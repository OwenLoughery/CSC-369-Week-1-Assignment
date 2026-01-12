#"C:\Users\rdlou\Downloads\2022_place_canvas_history.csv"

import csv
import operator
import time
from datetime import datetime

path = r"C:\Users\rdlou\Downloads\2022_place_canvas_history.csv"


def script(file, start, end):
    with open(file, "r", encoding="utf-8") as f:
        if end <= start:
            raise ValueError("start time must be less than end time")
        reader = csv.reader(f)
        header = next(reader)
        pixels = {}
        locs = {}
        for row in reader:
            strip = row[0][:13]
            time = datetime.strptime(strip, "%Y-%m-%d %H")

            if time < start:
                continue
            if time > end:
                continue
            if start <= time < end:
                if row[2] not in pixels:
                    pixels[row[2]] = 0
                pixels[row[2]] += 1
                if row[3] not in locs:
                    locs[row[3]] = 0
                locs[row[3]] += 1

        if not pixels or not locs:
            return None, None

        most_placed_color = max(pixels, key=pixels.get)
        most_placed_loc = max(locs, key=locs.get)
        x_str, y_str = most_placed_loc.split(",")
        most_placed_coord = (int(x_str), int(y_str))
        return most_placed_color, most_placed_coord




start_time = datetime.strptime("2022-04-01 12", "%Y-%m-%d %H")
end_time1 = datetime.strptime("2022-04-01 13", "%Y-%m-%d %H")
end_time2 = datetime.strptime("2022-04-01 15", "%Y-%m-%d %H")
end_time3 = datetime.strptime("2022-04-01 18", "%Y-%m-%d %H")

t0 = time.perf_counter_ns()
color, coord = script(path, start_time, end_time1)
t1 = time.perf_counter_ns()

elapsed_ms = (t1 - t0) / 1_000_000
print("Timeframe:", start_time, "to", end_time1)
print(f"Execution time: {elapsed_ms:.2f} ms")
print("Most placed color:", color)
print("Most placed pixel location:", coord)

t02 = time.perf_counter_ns()
color2, coord2 = script(path, start_time, end_time2)
t12 = time.perf_counter_ns()

elapsed_ms = (t12 - t02) / 1_000_000
print("Timeframe:", start_time, "to", end_time2)
print(f"Execution time: {elapsed_ms:.2f} ms")
print("Most placed color:", color2)
print("Most placed pixel location:", coord2)


t03 = time.perf_counter_ns()
color3, coord3 = script(path, start_time, end_time2)
t13 = time.perf_counter_ns()

elapsed_ms = (t13 - t03) / 1_000_000
print("Timeframe:", start_time, "to", end_time3)
print(f"Execution time: {elapsed_ms:.2f} ms")
print("Most placed color:", color3)
print("Most placed pixel location:", coord3)


'''
You will write a Python script that accepts a starting and ending hour as arguments and returns:

The most placed color during that timeframe.
The most placed pixel location during that timeframe.
Requirements
External Libraries: You are not allowed to use any external packages (nothing requiring pip install).

Input Format:

The script should accept start and end hours as command-line arguments in the following format:
YYYY-MM-DD HH (e.g., 2022-04-01 12 for April 1, 2022, at 12:00 PM).
Ensure your script validates that the end hour is after the start hour.
Color Format:
The colors in the dataset are stored as hexadecimal codes (e.g., #FFFFFF for white). You should return the most placed color in this format.

Timing the Script:
Use Python's time.perf_counter_ns() or equivalent to measure execution time.
'''