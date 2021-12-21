from functools import cache
from statistics import median

from run_util import run_puzzle


def part_a(data):
    positions = [int(x) for x in data.strip().split(',')]
    target_position = int(median(positions))
    return sum([abs(position - target_position) for position in positions])


def part_b(data):
    positions = [int(x) for x in data.strip().split(',')]

    @cache
    def cost_fn(d):
        return d * (d + 1) // 2

    costs = []
    for y in range(min(positions), max(positions) + 1):
        costs.append(sum([cost_fn(abs(x - y)) for x in positions]))
    return min(costs)


def main():
    examples = [
        ("""16,1,2,0,4,2,7,1,2,14""", 37, 168)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
