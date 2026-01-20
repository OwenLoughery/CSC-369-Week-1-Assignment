import pandas
import time
from datetime import datetime
import sys

path = r"2022_place_canvas_history.csv"



def most_placed_db(start, end, csv_path = path):
    start_t = pandas.to_datetime(start, format="%Y-%m-%d %H", utc=True)
    end_t = pandas.to_datetime(end, format="%Y-%m-%d %H", utc=True)

    if end_t <= start_t:
        raise ValueError("End hour must be after start hour.")

    cols = ["timestamp", "pixel_color", "coordinate"]

    pixels = {}
    coords = {}

    for chunk in pandas.read_csv(csv_path, usecols=cols, chunksize=500_000):
        chunk["ts"] = pandas.to_datetime(chunk["timestamp"], utc=True, errors="coerce")

        filtered = chunk[(chunk["ts"] >= start_t) & (chunk["ts"] < end_t)]
        if filtered.empty:
            continue

        vc_color = filtered["pixel_color"].value_counts()
        for color, n in vc_color.items():
            pixels[color] = pixels.get(color, 0) + int(n)

        vc_coord = filtered["coordinate"].value_counts()
        for coord, n in vc_coord.items():
            coords[coord] = coords.get(coord, 0) + int(n)
    if not pixels or not coords:
        return None, None
    most_color = max(pixels, key=pixels.get)
    most_coord = max(coords, key=coords.get)

    x_str, y_str = most_coord.split(",")
    most_placed_coord = (int(x_str), int(y_str))
    return most_color, most_placed_coord

def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python pandas_file.py "YYYY-MM-DD HH" "YYYY-MM-DD HH"')

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