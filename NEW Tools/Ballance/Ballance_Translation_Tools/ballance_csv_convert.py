"""
Copyright © 2026  Bartłomiej Duda
License: GPL-3.0 License
"""

import csv
from typing import List


def read_csv(filename, encoding="utf-8", delimiter="\t") -> List[List[str]]:
    with open(filename, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)
        return list(reader)


def write_csv(filename, rows, encoding="utf-8", delimiter="\t") -> None:
    with open(filename, "w", encoding=encoding, newline="") as f:
        writer = csv.writer(f, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        writer.writerows(rows)


def export_for_omegat(input_file_path: str, output_file_path: str) -> None:
    # rows = read_csv(input_file)
    pass  # TODO
