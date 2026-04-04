#!/usr/bin/python3
"""Module to print incoming stats."""
import sys

total_size = 0
status_counts = {}
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_counter = 0


def print_stats():
    """Print the code and count of it."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_counter += 1
            parts = line.strip().split()

            try:
                status = parts[-2]
                size = int(parts[-1])
                total_size += size

                if status in valid_codes:
                    status_counts[status] = status_counts.get(status, 0) + 1
            except (IndexError, ValueError):
                continue

            if line_counter % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()
