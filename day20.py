import time

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


def step(algo, image, default):
    rows = []
    cols = []
    for pixel in image:
        rows.append(pixel[0])
        cols.append(pixel[1])

    x_min = min(rows)
    x_max = max(rows)
    y_min = min(cols)
    y_max = max(cols)

    new_image = set()

    for x in range(x_min - 3, x_max + 4):
        for y in range(y_min - 3, y_max + 4):
            idx = 0
            n = -1
            for ny in (y + 1, y, y - 1):
                for nx in (x + 1, x, x - 1):
                    n += 1
                    if x_min <= nx <= x_max and y_min <= ny <= y_max:
                        if (nx, ny) in image:
                            idx += 2 ** n
                    else:
                        if default:
                            idx += 2 ** n

            if idx in algo:
                new_image.add((x, y))

    default = (511 if default else 0) in algo

    return frozenset(new_image), default


def enhance(algo, image, times):
    default = False

    image = frozenset(image)
    for _ in range(times):
        image, default = step(algo, image, default)

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
