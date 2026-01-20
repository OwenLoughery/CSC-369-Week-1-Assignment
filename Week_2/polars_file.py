import polars
import time
import sys
from datetime import datetime, timezone

path = r"2022_place_canvas_history.csv"



def most_placed_db(start, end, csv_path = path):
    start_t = datetime.strptime(start, "%Y-%m-%d %H").replace(tzinfo=timezone.utc)
    end_t = datetime.strptime(end, "%Y-%m-%d %H").replace(tzinfo=timezone.utc)

    if end_t <= start_t:
        raise ValueError("End hour must be after start hour.")

    df = polars.scan_csv(csv_path).select(
        ["timestamp", "pixel_color", "coordinate"]
    )

    df = df.with_columns(
        polars.col("timestamp")
        .str.strptime(
            polars.Datetime,
            format="%Y-%m-%d %H:%M:%S%.f UTC"
        )
        .dt.replace_time_zone("UTC")
        .alias("ts")
    )

    df = df.filter(
        (polars.col("ts") >= start_t) & (polars.col("ts") < end_t)
    )

    most_color = (
        df
        .group_by(polars.col("pixel_color"))
        .len()
        .sort("len", descending=True)
        .select("pixel_color")
        .limit(1)
        .collect()
    )

    most_coord = (
        df
        .group_by(polars.col("coordinate"))
        .len()
        .sort("len", descending=True)
        .select("coordinate")
        .limit(1)
        .collect()
    )

    if most_color.height == 0 or most_coord.height == 0:
        return None, None

    most_color = most_color[0, 0]
    most_coord = most_coord[0, 0]

    x_str, y_str = most_coord.split(",")
    most_placed_coord = (int(x_str), int(y_str))
    return most_color, most_placed_coord

def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python polars_file.py "YYYY-MM-DD HH" "YYYY-MM-DD HH"')

    start_hour = sys.argv[1]
    end_hour = sys.argv[2]

    t0 = time.perf_counter_ns()
    color, coord = most_placed_db(start_hour, end_hour)
    t1 = time.perf_counter_ns()

    elapsed_ms = (t1 - t0) / 1_000_000

    print(f"Timeframe: {start_hour} to {end_hour}")
    print(f"Execution time: {elapsed_ms:.2f} ms")
    print(f"Most placed color: {color}")
    print(f"Most placed pixel location: {coord}")


if __name__ == "__main__":
    main()