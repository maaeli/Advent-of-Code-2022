"""Test for the functions for the December 9 task."""


import pytest

from december10 import Processor, single_op, signal_strength


INSTRUCTIONS = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

image = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""


@pytest.mark.parametrize(
    "initial_clock, initial_X, operation, final_clock, final_X",
    [(0, 1, "noop", 1, 1), (1, 1, "addx 3", 3, 4), (3, 4, "addx -5", 5, -1)],
)
def test_single_op(initial_clock, initial_X, operation, final_clock, final_X):
    clock, X = single_op(initial_clock, initial_X, operation)
    assert clock == final_clock
    assert X == final_X


@pytest.mark.parametrize(
    "clock, X, signal",
    [
        (0, 1, 0),
        (1, 1, 1),
        (20, 21, 420),
        (60, 19, 1140),
        (100, 18, 1800),
        (140, 21, 2940),
    ],
)
def test_signal_strength(clock, X, signal):
    assert signal_strength(clock, X) == signal


def test_nth_X_manual_ops():
    proc = Processor(0, 1)
    proc.single_op("noop")
    assert proc.value_trace[1] == 1
    assert proc.value_trace == [1, 1]
    proc.single_op("addx 3")
    assert proc.value_trace[1] == 1
    assert proc.value_trace[2] == 1
    assert proc.value_trace[3] == 4
    assert proc.value_trace == [1, 1, 1, 4]
    proc.single_op("addx -5")
    assert proc.value_trace[1] == 1
    assert proc.value_trace[2] == 1
    assert proc.value_trace[3] == 4
    assert proc.value_trace[4] == 4
    assert proc.value_trace[5] == -1
    assert proc.value_trace == [1, 1, 1, 4, 4, -1]
    proc.single_op("noop")
    assert proc.value_trace == [1, 1, 1, 4, 4, -1, -1]
    proc.single_op("noop")
    assert proc.value_trace == [1, 1, 1, 4, 4, -1, -1, -1]
    proc.single_op("noop")
    proc.single_op("addx 0")
    assert proc.value_trace == [1, 1, 1, 4, 4, -1, -1, -1, -1, -1, -1]


def test_nth_X_op_list():
    proc = Processor(0, 1)
    proc.op_list(INSTRUCTIONS)
    print(proc.clock)
    assert proc.value_trace[20 - 1] == 21
    assert proc.value_trace[60 - 1] == 19
    assert proc.value_trace[100 - 1] == 18
    assert proc.value_trace[140 - 1] == 21
    assert proc.value_trace[180 - 1] == 16
    assert proc.value_trace[220 - 1] == 18


def test_total_signal():
    proc = Processor(0, 1)

    assert proc.op_list(INSTRUCTIONS).signal == 13140


def test_drawing():
    proc = Processor(0, 1)

    assert proc.op_list(INSTRUCTIONS).image(40, 6) == image
