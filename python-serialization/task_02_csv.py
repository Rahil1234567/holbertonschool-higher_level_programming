#!/usr/bin/python3
"""Converting CSV file to JSON file."""
import json
import csv


def convert_csv_to_json(csv_file):
    """Read csv file, convert it into dictionary, then serialize to json."""
    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
