"""Test for the functions for the December 9 task."""


import pytest

from december9 import Board

INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
INPUT2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


@pytest.mark.parametrize(
    "initial_positions, move, final_positions",
    [
        ({"H": (4, 0), "T": (4, 0)}, "R 4", {"H": (4, 4), "T": (4, 3)}),
        ({"H": (4, 4), "T": (4, 4)}, "L 4", {"H": (4, 0), "T": (4, 1)}),
        ({"H": (4, 4), "T": (4, 4)}, "L 0", {"H": (4, 4), "T": (4, 4)}),
        ({"H": (4, 4), "T": (4, 3)}, "U 1", {"H": (3, 4), "T": (4, 3)}),
        ({"H": (3, 4), "T": (4, 3)}, "U 1", {"H": (2, 4), "T": (3, 4)}),
        ({"H": (4, 4), "T": (4, 3)}, "U 4", {"H": (0, 4), "T": (1, 4)}),
        ({"H": (1, 5), "T": (1, 4)}, "D 1", {"H": (2, 5), "T": (1, 4)}),
        ({"H": (3, 3), "T": (4, 2)}, "U 1", {"H": (2, 3), "T": (3, 3)}),
    ],
)
def test_position_change(initial_positions, move, final_positions):
    board = Board(
        start_head=initial_positions["H"],
        start_tail=initial_positions["T"],
    )
    moved_board = board.move_head_and_tail(move)
    assert moved_board.head == final_positions["H"]
    assert moved_board.tail == final_positions["T"]


def test_visited():
    board = Board(start_head=(4, 0), start_tail=(4, 0))

    assert board.move_all(INPUT).visited_fields == 13


def test_long_rope():
    board = Board(start_head=(4, 0), start_tail=(4, 0), rope_el=10)

    assert board.move_all(INPUT2).visited_fields == 36
