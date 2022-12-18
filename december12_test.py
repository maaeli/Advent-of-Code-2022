"""Test for the functions for the December 12 task."""


from december12 import (
    get_shortest_path,
    get_start,
    get_end,
    find_scenic_route,
    get_any_start,
)


def test_get_shortest_path():
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    assert get_shortest_path(input) == 31


def test_get_start_example():
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    assert get_start(input) == (0, 0)


def test_get_end_example():
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    assert get_end(input) == (2, 5)


def test_get_start_non_trivial():
    input = """aabqponm
abcryxxl
accszExk
acctuvwS
abdefghi
"""
    assert get_start(input) == (3, 7)


def test_find_scenic_route():
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    assert find_scenic_route(input) == 29


def test_get_any_start():
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    assert get_any_start(input) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
    ]
