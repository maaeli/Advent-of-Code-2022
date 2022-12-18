"""Functions for the December 12 task."""

from helpers import split_input
import string
from copy import copy


def height(marker: str) -> int:
    if marker == "S":
        marker = "a"
    if marker == "E":
        marker = "z"
    alphabet = string.ascii_lowercase
    return alphabet.find(marker) + 1


def get_start(map: str):
    linear_index = map.find("S")
    line_length = map.find("\n", 1) + 1
    return (linear_index // line_length, linear_index % line_length)


def get_end(map: str):
    linear_index = map.find("E")
    line_length = map.find("\n", 1) + 1
    return (linear_index // line_length, linear_index % line_length)


def get_shortest_path(the_map: str) -> int:
    height_map = [
        [height(marker) for marker in line]
        for line in split_input(the_map, "\n")
    ]

    start = get_start(the_map)
    end = get_end(the_map)
    return way_finder(height_map, start, end)


def can_go_left(the_map, pos):
    return (
        pos[1] < len(the_map[0]) - 1
        and the_map[pos[0]][pos[1] + 1] <= the_map[pos[0]][pos[1]] + 1
    )


def can_go_right(the_map, pos):
    return (
        pos[1] > 0
        and the_map[pos[0]][pos[1] - 1] <= the_map[pos[0]][pos[1]] + 1
    )


def can_go_down(the_map, pos):
    return (
        pos[0] < len(the_map) - 1
        and the_map[pos[0] + 1][pos[1]] <= the_map[pos[0]][pos[1]] + 1
    )


def can_go_up(the_map, pos):
    return (
        pos[0] > 0
        and the_map[pos[0] - 1][pos[1]] <= the_map[pos[0]][pos[1]] + 1
    )


def way_finder(the_map, start, end, stop_at=1000):
    way = [start]
    routes = [way]
    visited_pos = [start]
    grow = True
    new_routes = []
    reaches_goal = []
    count = 0
    while grow:
        count += 1
        new_routes = []
        for way in routes:
            pos = way[-1]
            new_pos = []
            if can_go_left(the_map, pos):
                new_pos.append((pos[0], pos[1] + 1))
            if can_go_down(the_map, pos):
                new_pos.append((pos[0] + 1, pos[1]))
            if can_go_up(the_map, pos):
                new_pos.append((pos[0] - 1, pos[1]))
            if can_go_right(the_map, pos):
                new_pos.append((pos[0], pos[1] - 1))
            for npos in new_pos:
                if npos not in visited_pos:
                    visited_pos.append(npos)
                    new_way = copy(way)
                    new_way.append(npos)
                    if npos == end:
                        reaches_goal.append(new_way)
                        return count
                    else:
                        new_routes.append(new_way)
        routes = new_routes
        if routes == [] or count > stop_at:
            grow = False
    return 10**6


def find_scenic_route(the_map):
    height_map = [
        [height(marker) for marker in line]
        for line in split_input(the_map, "\n")
    ]

    start_points = get_any_start(the_map)
    end = get_end(the_map)
    min_route = get_shortest_path(the_map)
    for start in start_points:
        new_route = way_finder(height_map, start, end, stop_at=min_route)
        if new_route < min_route:
            min_route = new_route
    return min_route


def get_any_start(the_map: str):

    the_map = the_map.replace("S", "a")

    line_length = the_map.find("\n", 1) + 1
    linear_index = the_map.find("a")
    indexes = [(linear_index // line_length, linear_index % line_length)]
    while linear_index > -1:
        linear_index = the_map.find("a", linear_index + 1)
        if linear_index > -1:
            indexes.append(
                (linear_index // line_length, linear_index % line_length)
            )
    return indexes


if __name__ == "__main__":
    with open("december12_input.txt") as file:
        december12_map = file.read()

    print(
        "What is the fewest steps required to move from your current position to the location that should get the best signal?",
        get_shortest_path(december12_map),
    )
    print(
        "What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?",
        find_scenic_route(december12_map),
    )
