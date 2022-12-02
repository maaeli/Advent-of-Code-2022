"""Test for the functions for the December 2 task."""

from december2 import (
    Round,
    Choice,
    total_points,
    choice_for_outcome,
    round_for_outcome,
    total_points_for_outcomes,
)

EXAMPLE_SCORES = {"A Y": 8, "B X": 1, "C Z": 6}
EXAMPLE_RESULTS = """
A Y
B X
C Z
"""


def test_score_per_round():
    """Test whether the correct score is calculated for the example rounds."""
    for a_round, score in EXAMPLE_SCORES.items():
        assert score == Round(a_round).calculate_my_score()


def test_round_parsing():
    """Test whether each round represents the correct choices."""
    round1 = Round("A Y")
    round2 = Round("B X")
    round3 = Round("C Z")
    assert round1.mine == Choice.PAPER
    assert round1.theirs == Choice.ROCK
    assert round2.mine == Choice.ROCK
    assert round2.theirs == Choice.PAPER
    assert round3.mine == Choice.SCISSORS
    assert round3.theirs == Choice.SCISSORS


def test_choice_comparison():
    """Tests whether we compare Rock, Paper, Scissors correclty."""
    assert Choice.SCISSORS == Choice.SCISSORS
    assert Choice.SCISSORS > Choice.PAPER
    assert Choice.SCISSORS < Choice.ROCK

    assert Choice.PAPER == Choice.PAPER
    assert Choice.PAPER > Choice.ROCK
    assert Choice.PAPER < Choice.SCISSORS

    assert Choice.ROCK == Choice.ROCK
    assert Choice.ROCK > Choice.SCISSORS
    assert Choice.ROCK < Choice.PAPER


def test_total_points_example():
    """Test whether the total score for the example is correct."""
    assert total_points(EXAMPLE_RESULTS) == 15


def test_select_choice_for_outcome():
    """Test whether the correct choice for the desired outcome is made."""
    assert choice_for_outcome("A Y") == Choice.ROCK
    assert choice_for_outcome("B X") == Choice.ROCK
    assert choice_for_outcome("C Z") == Choice.ROCK


def test_round_for_given_outcome():
    """Test whether the correct round for the desired outcome is created."""
    round1 = round_for_outcome("A Y")
    round2 = round_for_outcome("B X")
    round3 = round_for_outcome("C Z")
    round4 = round_for_outcome("C Y")
    round5 = round_for_outcome("C X")

    assert round1.mine == Choice.ROCK
    assert round1.theirs == Choice.ROCK
    assert round2.mine == Choice.ROCK
    assert round2.theirs == Choice.PAPER
    assert round3.mine == Choice.ROCK
    assert round3.theirs == Choice.SCISSORS
    assert round4.mine == Choice.SCISSORS
    assert round4.theirs == Choice.SCISSORS
    assert round5.mine == Choice.PAPER
    assert round5.theirs == Choice.SCISSORS


def test_total_result_for_given_outcome():
    """Test whether the total resuls for the desired outcomes is computed"""
    assert total_points_for_outcomes(EXAMPLE_RESULTS) == 12
