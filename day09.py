import math

from aocd import get_data, submit

D_X = [-1, 0, 1, 0]
D_Y = [0, -1, 0, 1]
D_XY = list(zip(D_X, D_Y))


def get_neighbors(coords, x, y):
    neighbors = [(x + dx, y + dy) for dx, dy in D_XY if (x + dx, y + dy) in coords]
    return neighbors


def parse_data(data):
    return {
        (x, y): int(cell)
        for y, line in enumerate(data.split('\n'))
        for x, cell in enumerate(line)
    }


def part_a(data):
    coords = parse_data(data)

    risk = 0
    for point in coords.keys():
        neighbors = get_neighbors(coords, *point)
        assert len(neighbors) > 1
        own_value = coords[point]
        neighbor_values = [coords[neighbor] for neighbor in neighbors if neighbor in coords]
        if all([neighbor_value > own_value for neighbor_value in neighbor_values]):
            risk += 1 + own_value

    return risk


def part_b(data):
    coords = parse_data(data)

    low_points = []
    for point in coords.keys():
        neighbors = get_neighbors(coords, *point)

        own_value = coords[point]
        neighbor_values = [coords[neighbor] for neighbor in neighbors if neighbor in coords]
        if all([neighbor_value > own_value for neighbor_value in neighbor_values]):
            low_points.append(point)

    def expand(coords, points, point):
        if point not in coords or coords[point] == 9:
            return points

        points.add(point)
        neighbors = get_neighbors(coords, *point)

        for neighbor in neighbors:
            if neighbor not in points:
                points = points | expand(coords, points, neighbor)

        return points

    basins = {point: expand(coords, set(), point) for point in low_points}

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
