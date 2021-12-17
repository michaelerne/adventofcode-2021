from typing import Set, Tuple

from aocd import get_data, submit


def parse_data(data):
    # min_x, max_x, min_y, max_y = parse.parse('x={:d}..{:d}, y={:d}..{:d}', data).fixed

    data = data.split(': ')[1]
    data = data.replace('x=', '').replace('y=', '')
    x, y = data.split(', ')
    x_min, x_max = x.split('..')
    y_min, y_max = y.split('..')
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)

    target = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            target.add((x, y))

    return target, x_max, y_min


def simulate_shot(x, y, max_x, min_y) -> Set[Tuple[int, int]]:
    pos_x, pos_y = 0, 0
    hit = set()
    while pos_x <= max_x and pos_y >= min_y:
        pos_x += x
        pos_y += y
        x = max(x - 1, 0)
        y -= 1
        hit.add((pos_x, pos_y))
    return hit


def part_a(data):
    target, max_x, min_y = parse_data(data)

    highest = 0
    for x in range(200):
        for y in range(min_y, 200):
            hits = simulate_shot(x, y, max_x, min_y)
            if any([hit in target for hit in hits]):
                highest = max(highest, max(hits, key=lambda x: x[1])[1])
    return highest


def part_b(data):
    target, max_x, min_y = parse_data(data)

    works_count = 0
    for x in range(200):
        for y in range(min_y, 200):
            hits = simulate_shot(x, y, max_x, min_y)
            if any([hit in target for hit in hits]):
                works_count += 1
    return works_count


def main():
    data = get_data()

    example_data = """target area: x=20..30, y=-10..-5"""
    example_solution_a = 45
    example_solution_b = 112

    example_answer_a = part_a(example_data)
    assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
