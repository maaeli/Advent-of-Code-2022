"""Functions for the December 4 task."""

from typing import Tuple
from helpers import split_input


def parse_assignment(assignment: str) -> Tuple[int, int]:
    return tuple(int(range_limit) for range_limit in assignment.split("-"))


def complete_assignment_overlap(assignment_pair: str) -> bool:
    assignments = [
        parse_assignment(assignment)
        for assignment in assignment_pair.split(",")
    ]
    return (
        (assignments[0][0] <= assignments[1][0])
        & (assignments[0][1] >= assignments[1][1])
    ) | (
        (assignments[1][0] <= assignments[0][0])
        & (assignments[1][1] >= assignments[0][1])
    )


def partial_assignment_overlap(assignment_pair: str) -> bool:
    assignments = [
        parse_assignment(assignment)
        for assignment in assignment_pair.split(",")
    ]
    return (assignments[0][0] <= assignments[1][0] <= assignments[0][1]) | (
        assignments[1][0] <= assignments[0][0] <= assignments[1][1]
    )


def total_number_of_complete_overlap_pairs(assignment_list: str) -> int:
    return len(
        [
            pair
            for pair in split_input(assignment_list, "\n")
            if complete_assignment_overlap(pair)
        ]
    )


def total_number_of_partial_overlap_pairs(assignment_list: str) -> int:
    return len(
        [
            pair
            for pair in split_input(assignment_list, "\n")
            if partial_assignment_overlap(pair)
        ]
    )


if __name__ == "__main__":
    with open("december4_input.txt") as file:
        december4_assignments = file.read()
    print(
        "In how many assignment pairs does one range fully contain the other? ",
        total_number_of_complete_overlap_pairs(december4_assignments),
    )
    print(
        "In how many assignment pairs do the ranges overlap? ",
        total_number_of_partial_overlap_pairs(december4_assignments),
    )
