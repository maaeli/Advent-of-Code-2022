"""Test for the functions for the December 11 task."""


import pytest
from december11 import Monkey, process_round, monkey_business

demo_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


@pytest.mark.parametrize(
    "monkey_description, monkey_id",
    [(demo_input.split("\n\n")[i], i) for i in range(4)],
)
def test_init_monkey_id(monkey_description, monkey_id):
    monkey = Monkey(monkey_description)
    assert monkey.id == monkey_id


@pytest.mark.parametrize(
    "monkey_description, monkey_items",
    [
        (demo_input.split("\n\n")[0], [79, 98]),
        (demo_input.split("\n\n")[1], [54, 65, 75, 74]),
        (demo_input.split("\n\n")[2], [79, 60, 97]),
        (demo_input.split("\n\n")[3], [74]),
    ],
)
def test_init_monkey_items(monkey_description, monkey_items):
    monkey = Monkey(monkey_description)
    assert monkey.items == monkey_items


# @pytest.mark.parametrize(
#     "monkey_description, updated_levels",
#     [
#         (demo_input.split("\n\n")[0], [500, 620]),
#         (demo_input.split("\n\n")[1], [20, 23, 27, 26]),
#         (demo_input.split("\n\n")[2], [2080, 1200, 3136]),
#         (demo_input.split("\n\n")[3], [25]),
#     ],
# )
# def test_item_inspect(monkey_description, updated_levels):
#     monkey = Monkey(monkey_description)
#     monkey.inspect_items()
#     assert monkey.items == updated_levels


@pytest.mark.parametrize(
    "monkey_description, monkey_operator",
    [
        (demo_input.split("\n\n")[0], lambda x: x * 19),
        (demo_input.split("\n\n")[1], lambda x: x + 6),
        (demo_input.split("\n\n")[2], lambda x: x * x),
        (demo_input.split("\n\n")[3], lambda x: x + 3),
    ],
)
def test_init_monkey_operator(monkey_description, monkey_operator):
    monkey = Monkey(monkey_description)
    for i in range(100):
        assert monkey.operator(i) == monkey_operator(i)


@pytest.mark.parametrize(
    "monkey_description, monkey_trues, monkey_falses",
    [
        (demo_input.split("\n\n")[0], [0, 23, 46, 322], [1, 22, 24, 45, 47]),
        (demo_input.split("\n\n")[1], [0, 19, 38], [1, 18, 20]),
        (demo_input.split("\n\n")[2], [0, 13, 26], [1, 12, 14]),
        (demo_input.split("\n\n")[3], [0, 17, 34], [1, 12, 14, 23]),
    ],
)
def test_init_monkey_rule(monkey_description, monkey_trues, monkey_falses):
    monkey = Monkey(monkey_description)
    for number in monkey_trues:
        assert monkey.rule(number) == True
    for number in monkey_falses:
        assert monkey.rule(number) == False


@pytest.mark.parametrize(
    "monkey_description, target",
    [
        (demo_input.split("\n\n")[0], 2),
        (demo_input.split("\n\n")[1], 2),
        (demo_input.split("\n\n")[2], 1),
        (demo_input.split("\n\n")[3], 0),
    ],
)
def test_init_monkey_true_target(monkey_description, target):
    monkey = Monkey(monkey_description)
    assert monkey.true_target == target


@pytest.mark.parametrize(
    "monkey_description, target",
    [
        (demo_input.split("\n\n")[0], 3),
        (demo_input.split("\n\n")[1], 0),
        (demo_input.split("\n\n")[2], 3),
        (demo_input.split("\n\n")[3], 1),
    ],
)
def test_init_monkey_false_target(monkey_description, target):
    monkey = Monkey(monkey_description)
    assert monkey.false_target == target


def test_first_round():
    monkeys = [Monkey(description) for description in demo_input.split("\n\n")]
    monkeys = process_round(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


def test_20_round():
    monkeys = [Monkey(description) for description in demo_input.split("\n\n")]
    for _ in range(20):
        monkeys = process_round(monkeys)
    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


def test_number_of_inspections():
    monkeys = [Monkey(description) for description in demo_input.split("\n\n")]
    for _ in range(20):
        monkeys = process_round(monkeys)
    assert monkeys[0].inspections == 101
    assert monkeys[1].inspections == 95
    assert monkeys[2].inspections == 7
    assert monkeys[3].inspections == 105


def test_monkey_business():
    assert monkey_business(demo_input, rounds=20, panic_level=3) == 10605


def test_panicked_monkey_business():
    assert (
        monkey_business(demo_input, rounds=10000, panic_level=1) == 2713310158
    )
