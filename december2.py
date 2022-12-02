"""Functions for the December 2 task."""

from enum import Enum
from functools import total_ordering


@total_ordering
class Choice(Enum):
    """Representation of Rock, Paper & Scissor."""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    A = ROCK
    B = PAPER
    C = SCISSORS
    X = ROCK
    Y = PAPER
    Z = SCISSORS

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self == Choice.PAPER and other == Choice.SCISSORS:
                return True
            if self == Choice.ROCK and other == Choice.PAPER:
                return True
            if self == Choice.SCISSORS and other == Choice.ROCK:
                return True
            return False
        return NotImplemented


class Outcome(Enum):
    """Represenation of the result of a round."""

    THEY_WIN = 0
    DRAW = 1
    I_WIN = 2


class Round:
    """A single round."""

    POINTS_PER_ROUND = 3

    def __init__(self, round_string: str):
        self.theirs = Choice[round_string[0]]
        self.mine = Choice[round_string[-1]]
        if self.theirs == self.mine:
            self.outcome = Outcome.DRAW
        elif self.theirs > self.mine:
            self.outcome = Outcome.THEY_WIN
        else:
            self.outcome = Outcome.I_WIN

    def calculate_my_score(self) -> int:
        """Calculate the score of this round."""
        return self.mine.value + self.outcome.value * self.POINTS_PER_ROUND


def total_points(results: str) -> int:
    """Calculate the total number of points in a game."""
    return sum(
        [
            Round(round).calculate_my_score()
            for round in results.split("\n")
            if len(round) > 1
        ]
    )


if __name__ == "__main__":
    with open("december2_input.txt") as file:
        december2_game_result = file.read()
    print(december2_game_result)
    print(
        "Total number of points for me: ", total_points(december2_game_result)
    )
