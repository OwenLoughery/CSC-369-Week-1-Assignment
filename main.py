import csv
import sys
import time
from datetime import datetime


def parse_hour(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H")


def analyze(file_path: str, start: datetime, end: datetime):
    if end <= start:
        raise ValueError("End hour must be after start hour.")

    color_counts = {}
    loc_counts = {}

    with open(file_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            ts_i = header.index("timestamp")
            color_i = header.index("pixel_color")
            loc_i = header.index("coordinate")
        except ValueError:
            ts_i, color_i, loc_i = 0, 2, 3

        for row in reader:
            ts_str = row[ts_i][:16]
            row_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M")

            if start <= row_time < end:
                color = row[color_i]
                loc = row[loc_i]

                color_counts[color] = color_counts.get(color, 0) + 1
                loc_counts[loc] = loc_counts.get(loc, 0) + 1

    if not color_counts or not loc_counts:
        return None, None

    most_color = max(color_counts, key=color_counts.get)
    most_loc = max(loc_counts, key=loc_counts.get)

    x_str, y_str = most_loc.split(",")
    most_coord = (int(x_str), int(y_str))

    return most_color, most_coord


def run_and_time(file_path: str, start: datetime, end: datetime):
    t0 = time.perf_counter_ns()
    color, coord = analyze(file_path, start, end)
    t1 = time.perf_counter_ns()
    elapsed_ms = (t1 - t0) / 1_000_000
    return elapsed_ms, color, coord


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(
            'Usage: python week1.py "YYYY-MM-DD HH" "YYYY-MM-DD HH" <csv_path>'
        )

    start = parse_hour(sys.argv[1])
    end = parse_hour(sys.argv[2])
    path = sys.argv[3]

    ms, color, coord = run_and_time(path, start, end)
    print(f"Timeframe: {start} to {end}")
    print(f"Execution time: {ms:.2f} ms")
    print(f"Most placed color: {color}")
    print(f"Most placed pixel location: {coord}")
