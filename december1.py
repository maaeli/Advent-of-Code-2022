"""Functions for the December 1 task."""

from typing import List
from functools import lru_cache


def transform_to_int(strings: List[str]) -> List[int]:
    """Takes a list of strings and cast each element to int."""
    return [int(x) for x in strings if x != ""]


def load_list_per_elf(load_list: str) -> List[List[int]]:
    """Split the string giving all loads per elf."""
    return [
        transform_to_int(load.split("\n"))
        for load in load_list.split("\n\n")
        if load.split("\n")
    ]


@lru_cache(1)
def total_load_per_elf(load_list: str) -> List[int]:
    """Calculate the total load per elf based on the string giving all loads."""
    return [sum(elf_load) for elf_load in load_list_per_elf(load_list)]


def elf_with_largest_load(load_list: str) -> int:
    """Find the elf with the highest total load. Elfs are counted starting with 1."""
    loads = total_load_per_elf(load_list)
    return loads.index(max(loads)) + 1


def largest_load_per_elf(load_list: str) -> int:
    """Return the largest load any elf has to carry."""
    return max(total_load_per_elf(load_list))


if __name__ == "__main__":
    with open("december1_input.txt") as file:
        december1_load = file.read()
    print("Elf with largest load: ", elf_with_largest_load(december1_load))
    print("Largest laod of an elf: ", largest_load_per_elf(december1_load))
