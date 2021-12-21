from typing import List

from run_util import run_puzzle


def parse_data(data: str) -> List[int]:
    input = [int(x) for x in data.strip().split(',')]
    return [input.count(i) for i in range(9)]


def age(swarm: List[int]) -> List[int]:
    swarm = swarm[1:] + swarm[:1]
    swarm[6] += swarm[-1]
    return swarm


def part_a(data):
    swarm = parse_data(data)

    days = 80

    for _ in range(days):
        swarm = age(swarm)

    return sum(swarm)


def part_b(data):
    swarm = parse_data(data)

    days = 256

    for _ in range(days):
        swarm = age(swarm)

    return sum(swarm)


def main():
    examples = [
        ("""3,4,3,1,2""", 5934, 26984457539)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
