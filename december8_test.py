"""Test for the functions for the December 8 task."""


import pytest

from december8 import tree_is_visible, number_of_visible_trees, scenic_score


TEST_INPUT = """
30373
25512
65332
33549
35390
"""

UP_TEST = """
111
323
333
"""

DOWN_TEST = """
131
323
313
"""


def test_tree_is_visible():
    assert tree_is_visible(TEST_INPUT, position=(1, 1))
    assert tree_is_visible(TEST_INPUT, position=(1, 2))
    assert not tree_is_visible(TEST_INPUT, position=(1, 3))
    assert tree_is_visible(TEST_INPUT, position=(2, 1))
    assert not tree_is_visible(TEST_INPUT, position=(2, 2))
    assert not tree_is_visible(TEST_INPUT, position=(3, 3))

    assert tree_is_visible(UP_TEST, position=(1, 1))
    assert tree_is_visible(DOWN_TEST, position=(1, 1))


def test_scenic_score():

    assert scenic_score(TEST_INPUT, position=(1, 2)) == 4
    assert scenic_score(TEST_INPUT, position=(3, 2)) == 8


def test_number_of_visible_trees():
    assert number_of_visible_trees(TEST_INPUT) == 21
