from typing import List
from aocd import get_data, submit


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
    data = get_data()

    example_data = """3,4,3,1,2"""
    example_solution_a = 5934
    example_solution_b = 26984457539

    example_answer_a = part_a(example_data)
    assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_solution_a} != {example_answer_a}"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == example_solution_b, "example_data did not match for part_b"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
