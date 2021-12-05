from collections import defaultdict
from itertools import repeat
from typing import Tuple

import parse
from aocd import get_data, submit

Point = Tuple[int, int]


def parse_data(data):
    numbers = [parse.parse('{:d},{:d} -> {:d},{:d}', line).fixed for line in data.split('\n')]
    return [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in numbers]


def get_gen(x1, x2):
    if x1 == x2:
        return repeat(x1)
    step = -1 if x1 > x2 else 1
    return range(x1, x2 + step, step)


def get_points(p1: Point, p2: Point, allow_diagonal=False):
    x1, y1 = p1
    x2, y2 = p2

    if not allow_diagonal:
        if x1 != x2 and y1 != y2:
            return []

    x_gen = get_gen(x1, x2)
    y_gen = get_gen(y1, y2)

    return zip(x_gen, y_gen)


def part_a(data):
    lines = parse_data(data)
    map = defaultdict(int)

    for start, end in lines:
        for point in get_points(start, end):
            map[point] += 1

    count = len([x for x in map.values() if x >= 2])
    return count


def part_b(data):
    lines = parse_data(data)
    map = defaultdict(int)

    for start, end in lines:
        for point in get_points(start, end, allow_diagonal=True):
            map[point] += 1

    count = len([x for x in map.values() if x >= 2])
    return count


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
