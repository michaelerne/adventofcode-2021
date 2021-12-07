from functools import cache
from statistics import median

from aocd import get_data, submit


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
    data = get_data()

    example_data = """16,1,2,0,4,2,7,1,2,14"""
    example_solution_a = 37
    example_solution_b = 168

    example_answer_a = part_a(example_data)
    assert example_answer_a == example_solution_a, "example_data did not match for part_a"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == example_solution_b, "example_data did not match for part_b"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
