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

    def beats_me(self):
        if self == Choice.ROCK:
            return self.PAPER
        if self == Choice.PAPER:
            return Choice.SCISSORS
        return self.ROCK

    def i_beat(self):
        if self == Choice.ROCK:
            return self.SCISSORS
        if self == Choice.PAPER:
            return Choice.ROCK
        return self.PAPER


class Outcome(Enum):
    """Represenation of the result of a round."""

    THEY_WIN = 0
    DRAW = 1
    I_WIN = 2
    X = THEY_WIN
    Y = DRAW
    Z = I_WIN


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
    """Calculate the total number of points in a game for a given list of rounds."""
    return sum(
        [
            Round(round).calculate_my_score()
            for round in results.split("\n")
            if len(round) > 1
        ]
    )


def choice_for_outcome(outcome_description: str) -> Choice:
    """Determine which Choice I need for a given outcome."""
    if Outcome[outcome_description[-1]] == Outcome.DRAW:
        return Choice[outcome_description[0]]
    if Outcome[outcome_description[-1]] == Outcome.THEY_WIN:
        return Choice[outcome_description[0]].i_beat()
    return Choice[outcome_description[0]].beats_me()


def round_for_outcome(outcome_description: str) -> Round:
    """Find the round that produces a given outcome."""
    choice_to_letter = {
        Choice.ROCK: "A",
        Choice.PAPER: "B",
        Choice.SCISSORS: "C",
    }
    return Round(
        outcome_description[0:2]
        + choice_to_letter[choice_for_outcome(outcome_description)]
    )


def total_points_for_outcomes(outcomes: str) -> int:
    """Calculate the total number of points in a game for a given list of outcomes."""
    return sum(
        [
            round_for_outcome(round).calculate_my_score()
            for round in outcomes.split("\n")
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
    print(
        "Total number of points for me, producing outcome: ",
        total_points_for_outcomes(december2_game_result),
    )
