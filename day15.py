import time
from heapq import heappop, heappush

from aocd import get_data, submit

D_XY = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_data(data):
    lines = data.split('\n')
    return {
               (int(x), int(y)): int(risk)
               for y, line in enumerate(lines)
               for x, risk in enumerate(line)
           }, len(lines[0]), len(lines)


def get_neighbors(grid, x, y):
    return [(x + dx, y + dy) for dx, dy in D_XY if (x + dx, y + dy) in grid]


def get_shortest_path(grid, start, end):
    queue = [(0, start)]

    costs = {}

    while queue:
        cost, point = heappop(queue)
        if point == end:
            return cost

        for neighbor in get_neighbors(grid, *point):
            neighbor_cost = cost + grid[neighbor]
            if neighbor in costs and costs[neighbor] <= neighbor_cost:
                continue
            costs[neighbor] = neighbor_cost
            heappush(queue, (neighbor_cost, neighbor))


def expand_grid(grid, max_x, max_y, factor):
    expanded_max_x = max_x * factor
    expanded_max_y = max_y * factor

    return {
               # point: (seed value + distance - 1) % 9 + 1
               (x, y): (grid[(x % max_x, y % max_y)] + x // max_x + y // max_y - 1) % 9 + 1
               for x in range(expanded_max_x)
               for y in range(expanded_max_y)
           }, expanded_max_x, expanded_max_y


def part_a(data):
    grid, max_x, max_y = parse_data(data)

    answer = get_shortest_path(grid, (0, 0), (max_x - 1, max_y - 1))

    return answer


def part_b(data):
    grid, max_x, max_y = parse_data(data)

    grid, max_x, max_y = expand_grid(grid, max_x, max_y, factor=5)

    answer = get_shortest_path(grid, (0, 0), (max_x - 1, max_y - 1))

    return answer


def main():
    data = get_data()

    example_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    example_solution_a = 40
    example_solution_b = 315

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
