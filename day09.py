import math

from aocd import get_data, submit


def parse_data(data):
    return {
        (x, y): int(cell)
        for y, line in enumerate(data.split('\n'))
        for x, cell in enumerate(line)
    }


def part_a(data):
    coords = parse_data(data)

    risk = 0
    for x, y in coords.keys():
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), ]

        own_value = coords[(x, y)]
        neighbor_values = [coords[neighbor] for neighbor in neighbors if neighbor in coords]
        if all([neighbor_value > own_value for neighbor_value in neighbor_values]):
            risk += 1 + own_value

    return risk


def part_b(data):
    coords = parse_data(data)

    low_points = []
    for x, y in coords.keys():
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        own_value = coords[(x, y)]
        neighbor_values = [coords[neighbor] for neighbor in neighbors if neighbor in coords]
        if all([neighbor_value > own_value for neighbor_value in neighbor_values]):
            low_points.append((x, y))

    def expand(coords, points, x, y):
        if (x, y) not in coords or coords[(x, y)] == 9:
            return points

        points.add((x, y))
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for neighbor in neighbors:
            if neighbor not in points:
                points = points | expand(coords, points, *neighbor)

        return points

    basins = {(x, y): expand(coords, set(), x, y) for x, y in low_points}

    return math.prod([len(basin) for basin in sorted(basins.values(), key=len)[-3:]])


def main():
    data = get_data()

    example_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    example_solution_a = 15
    example_solution_b = 1134

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
