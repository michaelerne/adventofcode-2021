from collections import defaultdict
from itertools import repeat
from typing import Tuple

import parse

from run_util import run_puzzle

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
    examples = [
        ("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""", 5, 12)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
