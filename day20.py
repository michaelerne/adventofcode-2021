import time
from functools import cache

from aocd import get_data, submit

D_XY = [(dx, dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1)]


def parse_data(data):
    algo_data, img_data = data.split('\n\n')
    algo = {idx for idx, char in enumerate(algo_data) if char == '#'}
    image = {
        (x, y)
        for y, line in enumerate(img_data.split('\n'))
        for x, char in enumerate(line)
        if char == '#'
    }

    return algo, image


@cache
def get_neighbors(x, y):
    return [(x + dx, y + dy) for (dx, dy) in D_XY]


def step(algo, image, x_range, y_range, default):
    new_image = set()
    x_min, x_max = x_range[0], x_range[-1]
    y_min, y_max = y_range[0], y_range[-1]

    x_range = range(x_range[0] - 3, x_range[-1] + 4)
    y_range = range(y_range[0] - 3, y_range[-1] + 4)

    for x in x_range:
        for y in y_range:
            idx = 0
            for n, (nx, ny) in enumerate(reversed(get_neighbors(x, y))):
                if x_min <= nx <= x_max and y_min <= ny <= y_max:
                    if (nx, ny) in image:
                        idx += 2 ** n
                else:
                    if default:
                        idx += 2 ** n
            if idx in algo:
                new_image.add((x, y))

    default = (511 if default else 0) in algo

    return new_image, y_range, y_range, default


def enhance(algo, image, times):
    default = False
    x_range = range(max(image, key=lambda x: x[0])[0] + 1)
    y_range = range(max(image, key=lambda x: x[1])[1] + 1)

    for _ in range(times):
        image, x_range, y_range, default = step(algo, image, x_range, y_range, default)

    return image


def part_a(data):
    algo, image = parse_data(data)

    image = enhance(algo, image, 2)

    return len(image)


def part_b(data):
    algo, image = parse_data(data)

    image = enhance(algo, image, 50)

    return len(image)


def main():
    data = get_data()

    example_data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
    example_solution_a = 35
    example_solution_b = 3351

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
