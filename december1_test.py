"""Test for the functions for the December 1 task."""

from december1 import (
    elf_with_largest_load,
    largest_load_per_elf,
    total_load_per_elf,
    load_list_per_elf,
    transform_to_int,
)

EXAMPLE_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_total_load_example():
    """Using the provided example,
    test that the total load per elf is calculated correctly."""
    assert total_load_per_elf(EXAMPLE_INPUT) == [
        6000,
        4000,
        11000,
        24000,
        10000,
    ]


def test_load_example():
    """Using the provided example,
    test that the list of loads per elf is calculated correctly."""
    assert load_list_per_elf(EXAMPLE_INPUT) == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_transform_to_int():
    """Test that we correctly transform a list of strings
    to a list of ints, in case all elements are actually integers."""
    assert transform_to_int(["1", "2"]) == [1, 2]


def test_transform_to_int_with_emtpty_string():
    """Test that we correctly transform a list of strings
    to a list of ints,  in case one element is an empty string."""
    assert transform_to_int(["1", ""]) == [1]


def test_largest_load_per_elf_example():
    """Using the provided example,
    test that the largest load of any elf is calculated correctly."""
    assert largest_load_per_elf(EXAMPLE_INPUT) == 24000


def test_elf_with_largest_load_example():
    """Using the provided example,
    test that the elf with the largest load is determined correctly."""
    assert elf_with_largest_load(EXAMPLE_INPUT) == 4
