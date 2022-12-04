"""Test for the functions for the December 3 task."""


import pytest

from december3 import (
    compartment_load,
    shared_item,
    priority_of_item,
    priority_of_backpack,
    total_priority,
    badge_of_group,
    total_badge_priority,
)


@pytest.mark.parametrize(
    "complete_rucksack, first_compartment, second_compartment",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        (
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "jqHRNqRjqzjGDLGL",
            "rsFMfFZSrLrFZsSL",
        ),
        ("PmmdzqPrVvPwwTWBwg", "PmmdzqPrV", "vPwwTWBwg"),
    ],
)
def test_compartment_split(
    complete_rucksack, first_compartment, second_compartment
):
    assert compartment_load(complete_rucksack) == (
        first_compartment,
        second_compartment,
    )


@pytest.mark.parametrize(
    "complete_rucksack, shared_items",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", {"p"}),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", {"L"}),
        ("PmmdzqPrVvPwwTWBwg", {"P"}),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", {"v"}),
        ("ttgJtRGJQctTZtZT", {"t"}),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", {"s"}),
        ("abcdbc", {"b", "c"}),
    ],
)
def test_shared_item(complete_rucksack, shared_items):
    assert shared_item(complete_rucksack) == shared_items


@pytest.mark.parametrize(
    "item, priority",
    [("p", 16), ("L", 38), ("P", 42), ("v", 22), ("t", 20), ("s", 19)],
)
def test_priority_of_item(item, priority):
    assert priority_of_item(item) == priority


@pytest.mark.parametrize(
    "backpack, priority",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", 16),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38),
        ("PmmdzqPrVvPwwTWBwg", 42),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
        ("ttgJtRGJQctTZtZT", 20),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", 19),
        ("abcdbc", 5),
    ],
)
def test_priority_of_item(backpack, priority):
    assert priority_of_backpack(backpack) == priority


def test_total_priority():
    all_backpacks = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
    """
    assert total_priority(all_backpacks) == 157


@pytest.mark.parametrize(
    "backpacks, badge",
    [
        (
            (
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ),
            "r",
        ),
        (
            (
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ),
            "Z",
        ),
    ],
)
def test_badge_of_group(backpacks, badge):
    assert badge_of_group(backpacks) == badge


def test_total_badge_priority():
    all_backpacks = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
    """
    assert total_badge_priority(all_backpacks) == 70
