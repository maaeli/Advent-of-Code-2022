"""Functions for the December 3 task."""

from typing import Tuple, Set
import string


def compartment_load(complete_rucksack: str) -> Tuple[str, str]:
    compartment_size = len(complete_rucksack) // 2
    return (
        complete_rucksack[:compartment_size],
        complete_rucksack[compartment_size:],
    )


def shared_item(complete_rucksack: str) -> Set[str]:
    compartment1, compartment2 = compartment_load(complete_rucksack)
    return set(compartment1) & set(compartment2)


def priority_of_item(item: str) -> int:
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return alphabet.find(item) + 1


def priority_of_backpack(complete_rucksack: str) -> int:
    return sum(
        priority_of_item(item) for item in shared_item(complete_rucksack)
    )


def total_priority(all_backpacks: str) -> int:
    return sum(
        priority_of_backpack(backpack)
        for backpack in all_backpacks.split("\n")
        if backpack != ""
    )


if __name__ == "__main__":
    with open("december3_input.txt") as file:
        december3_backpacks = file.read()
    print("Load resorting priority: ", total_priority(december3_backpacks))
