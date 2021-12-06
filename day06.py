from aocd import get_data, submit
import parse
from typing import List
from collections import Counter

def age(swarm) -> List[int]:
    existing_swarm = []
    new_swarm = []
    for fish in swarm:
        if fish == 0:
            existing_swarm.append(6)
            new_swarm.append(8)
        else:
            existing_swarm.append(fish-1)
    return existing_swarm + new_swarm

def age2(swarm) -> Counter:
    new_swarm = Counter()

    new_swarm[0] = swarm[1]
    new_swarm[1] = swarm[2]
    new_swarm[2] = swarm[3]
    new_swarm[3] = swarm[4]
    new_swarm[4] = swarm[5]
    new_swarm[5] = swarm[6]
    new_swarm[6] = swarm[7]
    new_swarm[7] = swarm[8]

    new_swarm[6] += swarm[0]
    new_swarm[8] = swarm[0]

    return new_swarm



def part_a(data):
    swarm = [int(x) for x in data.strip().split(',')]

    days = 80

    for day in range(1, days+1):
        swarm = age(swarm)

    return len(swarm)


def part_b(data):
    swarm = Counter(int(x) for x in data.strip().split(','))

    days = 256

    print(f'initial state: {len(swarm)}')

    for day in range(1, days+1):
        swarm = age2(swarm)
        print(f'after day {day}: {sum(swarm.values())}')

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
