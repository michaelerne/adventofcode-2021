import heapq

from aocd import get_data, submit

D_XY = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_data(data):
    lines = data.split("\n")
    return [[int(pos) for pos in line] for line in lines], len(lines[0]), len(lines)


def get_neighbors(grid, point):
    x, y = point
    possible_neighbors = [(x + dx, y + dy) for dx, dy in D_XY]
    neighbors = [(x, y) for x, y in possible_neighbors if x in range(len(grid[0])) and y in range(len(grid))]
    return neighbors


def get_shortest_path(grid, start, end):
    q = [(0, *start)]

    costs = {}

    while heapq:
        cost, x, y = heapq.heappop(q)
        if (x, y) == end:
            return cost

        for n_x, n_y in get_neighbors(grid, (x, y)):
            n_c = cost + grid[n_x][n_y]
            if (n_x, n_y) in costs and costs[(n_x, n_y)] <= n_c:
                continue
            costs[(n_x, n_y)] = n_c
            heapq.heappush(q, (n_c, n_x, n_y))


def expand_grid(grid, factor):
    expanded = [[0 for _x in range(factor * len(grid[0]))] for _y in range(factor * len(grid))]

    for x in range(len(expanded)):
        for y in range(len(expanded[0])):
            dist = x // len(grid) + y // len(grid[0])
            newval = grid[x % len(grid)][y % len(grid[0])]
            for i in range(dist):
                newval += 1
                if newval == 10:
                    newval = 1
            expanded[x][y] = newval
    return expanded


def part_a(data):
    grid, max_x, max_y = parse_data(data)

    answer = get_shortest_path(grid, (0, 0), (max_x - 1, max_y - 1))

    return answer


def part_b(data):
    grid, max_x, max_y = parse_data(data)

    grid = expand_grid(grid, factor=5)
    answer = get_shortest_path(grid, (0, 0), (5 * max_x - 1, 5 * max_y - 1))

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
