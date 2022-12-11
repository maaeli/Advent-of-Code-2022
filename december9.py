"""Functions for the December 9 task."""

from helpers import split_input


class Board:
    def __init__(self, start_head=(0, 0), start_tail=(0, 0), rope_el=2):
        self.rope = [start_head for _ in range(rope_el)]
        self.rope[-1] = start_tail
        self.visited_places = {self.rope[0]}
        self.rope_el = rope_el

    @property
    def head(self):
        return self.rope[0]

    @property
    def tail(self):
        return self.rope[-1]

    def _pull_tail(self, head, tail):

        if abs(head[1] - tail[1]) == 1 and abs(head[0] - tail[0]) == 1:
            return tail
        elif head[1] - tail[1] > 1 and head[0] == tail[0]:
            tail = (tail[0], tail[1] + 1)
        elif tail[1] - head[1] > 1 and head[0] == tail[0]:
            tail = (tail[0], tail[1] - 1)
        elif head[1] - tail[1] > 1 and head[0] > tail[0]:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[1] - tail[1] > 1 and head[0] < tail[0]:
            tail = (tail[0] - 1, tail[1] + 1)
        elif tail[1] - head[1] > 1 and head[0] > tail[0]:
            tail = (tail[0] + 1, tail[1] - 1)
        elif tail[1] - head[1] > 1 and head[0] < tail[0]:
            tail = (tail[0] - 1, tail[1] - 1)
        elif head[0] - tail[0] > 1 and head[1] == tail[1]:
            tail = (head[0] - 1, tail[1])
        elif -head[0] + tail[0] > 1 and head[1] == tail[1]:
            tail = (head[0] + 1, tail[1])
        elif head[0] - tail[0] > 1 and head[1] > tail[1]:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] - tail[0] > 1 and head[1] < tail[1]:
            tail = (tail[0] + 1, tail[1] - 1)
        elif -head[0] + tail[0] > 1 and head[1] > tail[1]:
            tail = (tail[0] - 1, tail[1] + 1)
        elif -head[0] + tail[0] > 1 and head[1] < tail[1]:
            tail = (tail[0] - 1, tail[1] - 1)
        # self.visited_places.add(tail)
        return tail

    def move_head_and_tail(self, move):
        direction, distance_str = move.split(" ")
        distance = int(distance_str)

        if direction == "R":
            for _ in range(distance):
                self.rope[0] = (self.rope[0][0], self.rope[0][1] + 1)
                prev_seg = self.rope[0]
                for i, el in enumerate(self.rope[1:]):
                    # new_tail = self._pull_tail(new_head, new_tail)
                    el = self._pull_tail(prev_seg, el)
                    self.rope[i + 1] = el
                    prev_seg = el
                self.visited_places.add(self.rope[-1])
        if direction == "L":
            for _ in range(distance):
                self.rope[0] = (self.rope[0][0], self.rope[0][1] - 1)
                prev_seg = self.rope[0]
                for i, el in enumerate(self.rope[1:]):
                    # new_tail = self._pull_tail(new_head, new_tail)
                    el = self._pull_tail(prev_seg, el)
                    self.rope[i + 1] = el
                    prev_seg = el
                self.visited_places.add(self.rope[-1])
        if direction == "U":
            for _ in range(distance):
                self.rope[0] = (self.rope[0][0] - 1, self.rope[0][1])
                prev_seg = self.rope[0]
                for i, el in enumerate(self.rope[1:]):
                    # new_tail = self._pull_tail(new_head, new_tail)
                    el = self._pull_tail(prev_seg, el)
                    self.rope[i + 1] = el
                    prev_seg = el
                self.visited_places.add(self.rope[-1])
        if direction == "D":
            for _ in range(distance):
                self.rope[0] = (self.rope[0][0] + 1, self.rope[0][1])
                prev_seg = self.rope[0]
                for i, el in enumerate(self.rope[1:]):
                    # new_tail = self._pull_tail(new_head, new_tail)
                    el = self._pull_tail(prev_seg, el)

                    self.rope[i + 1] = el
                    prev_seg = el
                self.visited_places.add(self.rope[-1])
        return self

    def move_all(self, commands):
        for command in split_input(commands, "\n"):

            self.move_head_and_tail(command)
        return self

    @property
    def visited_fields(self):
        return len(self.visited_places)


if __name__ == "__main__":
    with open("december9_input.txt") as file:
        december9_moves = file.read()
    print(
        "How many positions does the tail of the rope visit at least once?",
        Board(start_head=(0, 0), start_tail=(0, 0))
        .move_all(december9_moves)
        .visited_fields,
    )
    print(
        "How many positions does the tail of the long rope visit at least once?",
        Board(start_head=(0, 0), start_tail=(0, 0), rope_el=10)
        .move_all(december9_moves)
        .visited_fields,
    )
