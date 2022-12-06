"""Test for the functions for the December 5 task."""


import pytest

from december5 import (
    parse_crates,
    single_move,
    process_all_moves,
    top_crates,
    process_crates,
    single_move_9001,
)

ORIGINAL_CRATES = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

SECOND_CRATES = """
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3
"""

SECOND_CRATES_9001 = SECOND_CRATES

THIRD_CRATES = """
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3"""

THIRD_CRATES_9001 = """
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3"""

FOURTH_CRATES = """
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
"""

FOURTH_CRATES_9001 = """
        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3 
"""

FINAL_CRATES = """
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
"""


FINAL_CRATES_9001 = """
        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
"""

MOVES = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

CRANE_INPUT = ORIGINAL_CRATES + MOVES


@pytest.mark.parametrize(
    "crate_string, crate_list",
    [
        (ORIGINAL_CRATES, [["Z", "N"], ["M", "C", "D"], ["P"]]),
        (SECOND_CRATES, [["Z", "N", "D"], ["M", "C"], ["P"]]),
        (THIRD_CRATES, [[], ["M", "C"], ["P", "D", "N", "Z"]]),
        (FOURTH_CRATES, [["C", "M"], [], ["P", "D", "N", "Z"]]),
        (FINAL_CRATES, [["C"], ["M"], ["P", "D", "N", "Z"]]),
    ],
)
def test_parse_crates(crate_string, crate_list):
    assert parse_crates(crate_string) == crate_list


@pytest.mark.parametrize(
    "initial_crates, move, resulting_crates",
    [
        (
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            "move 1 from 2 to 1",
            [["Z", "N", "D"], ["M", "C"], ["P"]],
        ),
        (
            [["Z", "N", "D"], ["M", "C"], ["P"]],
            "move 3 from 1 to 3",
            [[], ["M", "C"], ["P", "D", "N", "Z"]],
        ),
        (
            [[], ["M", "C"], ["P", "D", "N", "Z"]],
            "move 2 from 2 to 1",
            [["C", "M"], [], ["P", "D", "N", "Z"]],
        ),
        (
            [["C", "M"], [], ["P", "D", "N", "Z"]],
            "move 1 from 1 to 2",
            [["C"], ["M"], ["P", "D", "N", "Z"]],
        ),
    ],
)
def test_single_move(initial_crates, move, resulting_crates):
    assert single_move(initial_crates, move) == resulting_crates


@pytest.mark.parametrize(
    "initial_crates, move, resulting_crates",
    [
        (
            parse_crates(ORIGINAL_CRATES),
            "move 1 from 2 to 1",
            parse_crates(SECOND_CRATES_9001),
        ),
        (
            parse_crates(SECOND_CRATES_9001),
            "move 3 from 1 to 3",
            parse_crates(THIRD_CRATES_9001),
        ),
        (
            parse_crates(THIRD_CRATES_9001),
            "move 2 from 2 to 1",
            parse_crates(FOURTH_CRATES_9001),
        ),
        (
            parse_crates(FOURTH_CRATES_9001),
            "move 1 from 1 to 2",
            parse_crates(FINAL_CRATES_9001),
        ),
    ],
)
def test_single_move_9001(initial_crates, move, resulting_crates):
    assert single_move_9001(initial_crates, move) == resulting_crates


def test_all_moves():
    assert process_all_moves(
        parse_crates(ORIGINAL_CRATES), MOVES
    ) == parse_crates(FINAL_CRATES)


def test_all_moves_9001():
    assert process_all_moves(
        parse_crates(ORIGINAL_CRATES), MOVES, 9001
    ) == parse_crates(FINAL_CRATES_9001)


def test_top_crates():
    assert top_crates(parse_crates(FINAL_CRATES)) == "CMZ"


def test_crane_operation():
    assert process_crates(CRANE_INPUT) == "CMZ"


def test_crane_operation_9001():
    assert process_crates(CRANE_INPUT, 9001) == "MCD"
