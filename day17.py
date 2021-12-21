import math

import parse

from run_util import run_puzzle


def parse_data(data):
    return parse.parse('target area: x={:d}..{:d}, y={:d}..{:d}', data).fixed


def get_x(x):
    x_pos = 0
    while True:
        yield x_pos
        x_pos += x
        x = max(x - 1, 0)


def get_y(y):
    y_pos = 0
    while True:
        yield y_pos
        y_pos += y
        y -= 1


def simulate_shot(x, y, x_min, x_max, y_min, y_max) -> bool:
    x_gen = get_x(x)
    y_gen = get_y(y)

    point = zip(x_gen, y_gen)

    x, y = next(point)
    while x <= x_max and y >= y_min:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        x, y = next(point)

    return False


def part_a(data):
    x_min, x_max, y_min, y_max = parse_data(data)

    return (y_min * (y_min + 1)) // 2


def part_b(data):
    x_min, x_max, y_min, y_max = parse_data(data)

    x_vel_min = math.floor(0.5 * math.sqrt(8 * x_min + 1) - 1)
    x_vel_max = x_max
    y_vel_min = y_min
    y_vel_max = -y_min

    return sum([
        simulate_shot(x, y, x_min, x_max, y_min, y_max)
        for x in range(x_vel_min, x_vel_max + 1)
        for y in range(y_vel_min, y_vel_max + 1)
    ])


def main():
    examples = [
        ("""target area: x=20..30, y=-10..-5""", 45, 112)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
