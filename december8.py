"""Functions for the December 8 task."""

from typing import Tuple
from helpers import split_input
from functools import lru_cache
from itertools import product


@lru_cache(1)
def _tree_map_to_list(tree_map: str):
    return [[int(x) for x in line] for line in split_input(tree_map, "\n")]


def tree_is_visible(tree_map: str, position: Tuple[int, int]):
    row, column = position
    trees = [[int(x) for x in line] for line in _tree_map_to_list(tree_map)]
    tree_height = trees[row][column]
    if max(trees[row][:column]) < tree_height:
        return True
    if max(trees[row][column + 1 :]) < tree_height:
        return True
    if max([arow[column] for arow in trees[:row]]) < tree_height:
        return True
    if max([arow[column] for arow in trees[row + 1 :]]) < tree_height:
        return True
    return False


def number_of_visible_trees(tree_map: str):
    trees = _tree_map_to_list(tree_map)
    nr_rows = len(trees)
    nr_columns = len(trees[0])

    return (
        len(
            [
                pos
                for pos in product(
                    range(1, nr_rows - 1), range(1, nr_columns - 1)
                )
                if tree_is_visible(tree_map, pos)
            ]
        )
        + 2 * nr_rows
        + 2 * (nr_columns - 2)
    )


if __name__ == "__main__":
    with open("december8_input.txt") as file:
        december8_maps = file.read()
    print(
        "how many trees are visible from outside the grid? ",
        number_of_visible_trees(december8_maps),
    )
