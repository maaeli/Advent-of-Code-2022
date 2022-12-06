"""Functions for the December 5 task."""

from typing import List
from parse import parse
from helpers import split_input


def parse_crates(crates_string: str) -> List[List[str]]:
    crate_lines = split_input(crates_string, "\n")
    return [
        [c for c in i if c != " "]
        for i in zip(
            *[list(line[1::4]) for line in reversed(crate_lines[:-1])]
        )
    ]


def single_move(initial_crates: List[List[str]], move: str) -> List[List[str]]:
    """move 1 from 2 to 1"""
    parsed_move = parse(
        "move {nr_crates:d} from {origin:d} to {destination:d}", move
    )
    for _ in range(parsed_move["nr_crates"]):
        initial_crates[parsed_move["destination"] - 1].append(
            initial_crates[parsed_move["origin"] - 1].pop()
        )
    return initial_crates


def single_move_9001(
    initial_crates: List[List[str]], move: str
) -> List[List[str]]:
    """move 1 from 2 to 1"""
    parsed_move = parse(
        "move {nr_crates:d} from {origin:d} to {destination:d}", move
    )
    initial_crates[parsed_move["destination"] - 1].extend(
        initial_crates[parsed_move["origin"] - 1][-parsed_move["nr_crates"] :]
    )
    del initial_crates[parsed_move["origin"] - 1][-parsed_move["nr_crates"] :]
    return initial_crates


def process_all_moves(
    crates: List[List[str]], moves: str, model=9000
) -> List[List[str]]:
    split_input(moves, "\n")
    mover = single_move if model == 9000 else single_move_9001
    for move in split_input(moves, "\n"):
        crates = mover(crates, move)
    return crates


def top_crates(crates: List[List[str]]) -> str:
    return "".join([column.pop() for column in crates])


def process_crates(operation_description, model=9000) -> str:
    initial_crates, moves = operation_description.split("\n\n")
    return top_crates(
        process_all_moves(parse_crates(initial_crates), moves, model)
    )


if __name__ == "__main__":
    with open("december5_input.txt") as file:
        december5_crane_movement = file.read()
    print("Final configuration: ", process_crates(december5_crane_movement))
    print(
        "Final configuration using crane 9001: ",
        process_crates(december5_crane_movement, 9001),
    )
