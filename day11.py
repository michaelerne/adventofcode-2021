from collections import deque

from aocd import get_data, submit

D_XY = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]  # (0, 0) omitted


def parse_data(data):
    return {
        (x, y): int(val) for
        x, line in enumerate(data.split('\n'))
        for y, val in enumerate(line)
    }


def process_step(grid):
    to_flash = deque()
    flashed = set()

    for point, value in grid.items():
        value += 1
        grid[point] = value
        if value > 9:
            to_flash.append(point)
            flashed.add(point)

    while to_flash:
        x, y = to_flash.pop()
        neighbors = [(x + dx, y + dy) for dx, dy in D_XY if (x + dx, y + dy) in grid]
        for point in neighbors:
            value = grid[point] + 1
            grid[point] = value
            if value > 9 and point not in flashed:
                to_flash.append(point)
                flashed.add(point)

    for x, y in flashed:
        grid[x, y] = 0

    return grid, flashed


def part_a(data):
    grid = parse_data(data)

    answer = 0
    for _ in range(100):
        grid, flashed = process_step(grid)
        answer += len(flashed)

    return answer


def part_b(data):
    grid = parse_data(data)

    total = len(grid)
    step = 0
    while True:
        step += 1
        grid, flashed = process_step(grid)
        if len(flashed) == total:
            return step


def main():
    data = get_data()

    example_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    example_solution_a = 1656
    example_solution_b = 195

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