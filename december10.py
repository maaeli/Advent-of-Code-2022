"""Functions for the December 10 task."""

from typing import Tuple
from helpers import split_input

OP_TIMES = {"noop": 1, "addx": 2}


class Processor:
    def __init__(self, start_time: int, initial_X: int):
        self.clock = start_time
        self.X = initial_X
        self.value_trace = [initial_X]

    @property
    def signal(self):
        signal_points = [20, 60, 100, 140, 180, 220]
        return sum(
            signal_strength(i, self.value_trace[i - 1]) for i in signal_points
        )

    def single_op(self, operation: str):
        new_clock, new_X = single_op(self.clock, self.X, operation)
        for _ in range(self.clock + 1, new_clock):
            self.value_trace.append(self.X)
        self.value_trace.append(new_X)
        self.X = new_X
        self.clock = new_clock

    def op_list(self, instructions):
        for instruction in split_input(instructions, "\n"):
            self.single_op(instruction)
        return self

    def image(self, columns, rows):
        s = "\n"
        for r in range(rows):
            for time in range(columns):
                sprite_center = self.value_trace[time + columns * r]
                sprite = [sprite_center - 1, sprite_center, sprite_center + 1]
                if time in sprite:
                    s += "#"
                else:
                    s += "."
            s += "\n"
        return s


def single_op(
    initial_clock: int, initial_X: int, operation: str
) -> Tuple[int, int]:
    if operation == "noop":
        return initial_clock + OP_TIMES[operation], initial_X
    command, value = operation.split(" ")
    if command == "addx":
        return initial_clock + OP_TIMES[command], initial_X + int(value)


def signal_strength(clock, X):
    return clock * X


if __name__ == "__main__":
    with open("december10_input.txt") as file:
        december10_instructions = file.read()
    print("Signal", Processor(0, 1).op_list(december10_instructions).signal)
    print(
        "Image", Processor(0, 1).op_list(december10_instructions).image(40, 6)
    )
