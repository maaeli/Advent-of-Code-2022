"""Recurring functions needed for more then one day."""

from typing import List


def split_input(input: str, sep: str) -> List[str]:
    return [line for line in input.split(sep) if line != ""]
