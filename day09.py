from aocd import get_data, submit
import parse


def parse_data(data):
    coords = {}
    lines = data.split('\n')
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            coords[(x, y)] = int(col)
    return coords


def part_a(data):
    coords = parse_data(data)

    risk = 0
    for x, y in coords.keys():
        neighbors = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]

        own_val = coords[(x, y)]
        neighbor_vals = []
        for neighbor in neighbors:
            if neighbor in coords:
                neighbor_vals.append(coords[neighbor])
        if all([neighbor_val > own_val for neighbor_val in neighbor_vals]):
            risk += 1 + own_val

    return risk


def part_b(data):
    coords = parse_data(data)

    low_points = []
    for x, y in coords.keys():
        neighbors = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]

        own_val = coords[(x, y)]
        neighbor_vals = []
        for neighbor in neighbors:
            if neighbor in coords:
                neighbor_vals.append(coords[neighbor])
        if all([neighbor_val > own_val for neighbor_val in neighbor_vals]):
            low_points.append((x, y))

    def expand(coords, points, x, y):
        if (x, y) not in coords or coords[(x, y)] == 9:
            return points

        points.add((x, y))
        neighbors = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]
        for neighbor in neighbors:
            if neighbor not in points:
                new_points = expand(coords, points, *neighbor)
                points = points | new_points

        return points

    basins = {}
    for x, y in low_points:
        basins[(x, y)] = expand(coords, set(), x, y)

    basins = list(basins.values())
    basins_lens = [len(basin) for basin in basins]
    top_3 = sorted(basins_lens, reverse=True)[:3]
    return top_3[0] * top_3[1] * top_3[2]

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
