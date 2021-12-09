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


def get_lowest_points(grid):
    lowest_points = []
    for point in grid.keys():
        neighbors = get_neighbors(grid, *point)
        own_value = grid[point]
        neighbor_values = [grid[neighbor] for neighbor in neighbors if neighbor in grid]
        if all([neighbor_value > own_value for neighbor_value in neighbor_values]):
            lowest_points.append(point)
    return lowest_points



def part_a(data):
    grid = parse_data(data)

    risk = sum([1 + grid[point] for point in get_lowest_points(grid)])

    return risk


def part_b(data):
    grid = parse_data(data)

    lowest_points = get_lowest_points(grid)

    def expand(grid, seen, point):
        if point not in grid or grid[point] == 9:
            return seen

        seen.add(point)
        neighbors = get_neighbors(grid, *point)

        for neighbor in neighbors:
            if neighbor not in seen:
                seen = seen | expand(grid, seen, neighbor)

        return seen

    basins = {point: expand(grid, set(), point) for point in lowest_points}

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
