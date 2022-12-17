"""Functions for the December 11 task."""

from typing import List
from math import prod
from parse import parse


class Monkey:
    def __init__(self, description: str):
        description_lines = description.split("\n")
        self.id = parse("Monkey {id:d}:", description_lines[0])["id"]
        self.items = [
            int(item)
            for item in parse(
                "{}Starting items:{items}", description_lines[1]
            )["items"].split(",")
        ]
        self.operator = _operator_from_string(
            parse("{}Operation: new = {op}", description_lines[2])["op"]
        )
        # self.rule = _rule_from_string(
        #     parse("{}Test: {rule}", description_lines[3])["rule"]
        # )

        self.multiple = parse(
            "{}divisible by {multiple:d}", description_lines[3]
        )["multiple"]
        self.true_target = parse(
            "{}If true: throw to monkey {target:d}", description_lines[4]
        )["target"]
        self.false_target = parse(
            "{}If false: throw to monkey {target:d}", description_lines[5]
        )["target"]
        self.inspections = 0

    def inspect_items(self, shared_multiple=1, panic_level=3):
        if panic_level > 1:
            self.items = [
                (self.operator(item) // panic_level) for item in self.items
            ]
        else:
            self.items = [
                (self.operator(item % shared_multiple) // panic_level)
                for item in self.items
            ]
        self.inspections += len(self.items)

    def rule(self, x):
        if x % self.multiple == 0:
            return True
        return False


def _rule_from_string(op_string: str):
    divisor = parse("divisible by {divisor:d}", op_string)["divisor"]

    def f(x):
        if x % divisor == 0:
            return True
        return False

    return f


def _operator_from_string(op_string: str):
    _, operator, operand2 = op_string.split(" ")

    if operator == "*":

        def f(x):
            if operand2 == "old":
                a = x
            else:
                a = int(operand2)
            return x * a

    if operator == "+":

        def f(x):
            if operand2 == "old":
                a = x
            else:
                a = int(operand2)
            return x + a

    return f


def process_round(monkey_gang: List[Monkey], shared_multiple=1, panic_level=3):
    for monkey in monkey_gang:
        monkey.inspect_items(
            shared_multiple=shared_multiple, panic_level=panic_level
        )
        for item in monkey.items:
            target = (
                monkey.true_target
                if monkey.rule(item)
                else monkey.false_target
            )
            monkey_gang[target].items.append(item)
        monkey.items = []
    return monkey_gang


def business(monkey_gang: List[Monkey]):
    inspection_levels = sorted([monkey.inspections for monkey in monkey_gang])
    return inspection_levels[-2] * inspection_levels[-1]


def monkey_business(monkey_gang_description, rounds=20, panic_level=3):
    monkey_gang = [
        Monkey(description)
        for description in monkey_gang_description.split("\n\n")
    ]
    shared_multiple = prod(monkey.multiple for monkey in monkey_gang)
    for _ in range(rounds):
        monkey_gang = process_round(
            monkey_gang,
            shared_multiple=shared_multiple,
            panic_level=panic_level,
        )
    return business(monkey_gang)


if __name__ == "__main__":
    with open("december11_input.txt") as file:
        december11_instructions = file.read()
    print(
        "What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? ",
        monkey_business(december11_instructions),
    )
    print(
        "What is the level of monkey business after 10000 panicked rounds? ",
        monkey_business(december11_instructions, rounds=10000, panic_level=1),
    )
