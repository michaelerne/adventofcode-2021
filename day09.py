import math
from collections import deque

from run_util import run_puzzle

D_X = [-1, 0, 1, 0]
D_Y = [0, -1, 0, 1]
D_XY = list(zip(D_X, D_Y))


def get_neighbors(grid, x, y):
    return [
        (x + dx, y + dy)
        for dx, dy in D_XY if (x + dx, y + dy) in grid
    ]


def parse_data(data):
    return {
        (x, y): int(cell)
        for y, line in enumerate(data.split('\n'))
        for x, cell in enumerate(line)
    }


def get_lowest_points(grid):
    return [
        point
        for point in grid.keys()
        if all([grid[neighbor] > grid[point] for neighbor in get_neighbors(grid, *point) if neighbor in grid])
    ]


def part_a(data):
    grid = parse_data(data)

    return sum([
        1 + grid[point]
        for point in get_lowest_points(grid)
    ])


def get_basin(grid, point):
    basin = {point}
    queue = deque(basin)

    while queue:
        point = queue.pop()
        for neighbor in get_neighbors(grid, *point):
            if neighbor not in basin and grid[neighbor] != 9:
                basin.add(neighbor)
                queue.append(neighbor)

    return basin


def part_b(data):
    grid = parse_data(data)

    basins = {
        point: get_basin(grid, point)
        for point in get_lowest_points(grid)
    }

    return math.prod([
        len(basin)
        for basin in sorted(basins.values(), key=len)[-3:]
    ])


def main():
    examples = [
        ("""2199943210
3987894921
9856789892
8767896789
9899965678""", 15, 1134)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
