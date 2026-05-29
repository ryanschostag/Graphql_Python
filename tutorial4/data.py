import csv
from pathlib import Path


def read_file():
    file_path = Path(__file__).resolve().parent / "data.csv"
    with open(file_path) as f1:
        data = csv.reader(f1, delimiter=",")
        li = []
        i = 0
        for row in data:
            if i > 0:
                li.append({
                    "name": row[0],
                    "city": row[1],
                    "designation": row[2],
                    "experience_in_year": row[3],
                })
            i += 1

    return li