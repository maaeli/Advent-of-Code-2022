"""Test for the functions for the December 4 task."""


import pytest

from december4 import (
    parse_assignment,
    complete_assignment_overlap,
    total_number_of_complete_overlap_pairs,
)


@pytest.mark.parametrize(
    "pair, full_subset",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", False),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", False),
    ],
)
def test_complete_assignment_overlap(pair, full_subset):
    assert complete_assignment_overlap(pair) == full_subset


@pytest.mark.parametrize(
    "assignment_string, assignment_tuple",
    [
        ("2-4", (2, 4)),
        ("6-8", (6, 8)),
        ("2-3", (2, 3)),
        ("4-5", (4, 5)),
        ("5-7", (5, 7)),
        ("7-9", (7, 9)),
        ("2-8", (2, 8)),
        ("3-7", (3, 7)),
        ("6-6", (6, 6)),
        ("4-6", (4, 6)),
        ("2-6", (2, 6)),
        ("4-8", (4, 8)),
    ],
)
def test_parse_assignment(assignment_string, assignment_tuple):
    assert parse_assignment(assignment_string) == assignment_tuple


def test_total_number_of_complete_overlap_pairs():
    test_input = """
    2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
    assert total_number_of_complete_overlap_pairs(test_input) == 2
