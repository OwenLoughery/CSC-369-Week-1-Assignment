import duckdb
import time
from datetime import datetime
import sys

path = r"2022_place_canvas_history.csv"

con = duckdb.connect()

con.execute(f"""
        CREATE OR REPLACE VIEW place AS
        SELECT timestamp, pixel_color, coordinate
        FROM read_csv_auto('{path}', header=true);
    """)

def most_placed_db(start, end):
    start_t = datetime.strptime(start, "%Y-%m-%d %H")
    end_t = datetime.strptime(end, "%Y-%m-%d %H")
    if end_t <= start_t:
        raise ValueError("End hour must be after start hour.")

    color_row = con.execute(
        """
        SELECT 
            pixel_color, 
            COUNT(*) AS cnt
        FROM 
            place
        WHERE 
            timestamp >= ? 
            AND timestamp < ?
        GROUP BY pixel_color
        ORDER BY cnt DESC
        LIMIT 1;
        """,
        [start_t, end_t],
    ).fetchone()

    coord_row = con.execute(
        """
        SELECT 
            coordinate, 
            COUNT(*) AS cnt
        FROM 
            place
        WHERE 
            timestamp >= ? 
            AND timestamp < ?
        GROUP BY coordinate
        ORDER BY cnt DESC
        LIMIT 1;
        """,
        [start_t, end_t],
    ).fetchone()

    if color_row is None or coord_row is None:
        return None, None

    most_color = color_row[0]
    coord_str = coord_row[0]
    x_str, y_str = coord_str.split(",")
    most_coord = (int(x_str), int(y_str))

    return most_color, most_coord



def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python duckdb_file.py "YYYY-MM-DD HH" "YYYY-MM-DD HH"')

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