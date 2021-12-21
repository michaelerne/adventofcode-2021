from heapq import heappop, heappush

from run_util import run_puzzle

D_XY = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_data(data):
    return {
        (int(x), int(y)): int(risk)
        for y, line in enumerate(data.split('\n'))
        for x, risk in enumerate(line)
    }


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


def expand_grid(grid, factor):
    dimension_x, dimension_y = [x + 1 for x in max(grid, key=lambda x: x[0] * x[1])]

    return {
        # point: (seed value + distance - 1) % 9 + 1
        (x, y): (grid[(x % dimension_x, y % dimension_y)] + x // dimension_x + y // dimension_y - 1) % 9 + 1
        for x in range(dimension_x * factor)
        for y in range(dimension_y * factor)
    }


def part_a(data):
    grid = parse_data(data)

    max_x, max_y = max(grid, key=lambda x: x[0] * x[1])

    answer = get_shortest_path(grid, (0, 0), (max_x, max_y))

    return answer


def part_b(data):
    grid = parse_data(data)

    grid = expand_grid(grid, factor=5)

    max_x, max_y = max(grid, key=lambda x: x[0] * x[1])

    answer = get_shortest_path(grid, (0, 0), (max_x, max_y))

    return answer


def main():
    examples = [
        ("""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""", 40, 315)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
