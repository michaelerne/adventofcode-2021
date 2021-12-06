from collections import Counter

from aocd import get_data, submit


def parse_data(data: str) -> Counter[int]:
    return Counter(int(x) for x in data.strip().split(','))


def age(swarm) -> Counter:
    new_swarm = Counter()

    for index in range(0, 8):
        new_swarm[index] = swarm[index+1]

    new_swarm[6] += swarm[0]
    new_swarm[8] = swarm[0]

    return new_swarm


def part_a(data):
    swarm = parse_data(data)

    days = 80

    for _ in range(days):
        swarm = age(swarm)

    return len(swarm)


def part_b(data):
    swarm = parse_data(data)

    days = 256

    for _ in range(days):
        swarm = age(swarm)

    return sum(swarm.values())


def main():
    data = get_data()

    example_data = """3,4,3,1,2"""

    example_answer_a = part_a(example_data)
    assert example_answer_a == 5934, "example_data did not match for part_a"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == 26984457539, "example_data did not match for part_b"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
