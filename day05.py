from collections import defaultdict

from aocd import get_data, submit


def part_a(data):
    data_lines = data.split('\n')
    lines = []
    for data_line in data_lines:
        left, _, right = data_line.split(' ')
        from_x, from_y = left.split(',')
        to_x, to_y = right.split(',')
        lines.append([[int(from_x), int(from_y)], [int(to_x), int(to_y)]])

    map = defaultdict(lambda: 0)

    for from_c, to_c in lines:
        from_x, from_y = from_c
        to_x, to_y = to_c

        if from_x == to_x and from_y != to_y:
            # vertical
            min_val = min(from_y, to_y)
            max_val = max(from_y, to_y)
            vals = list(range(min_val, max_val + 1))
            for y in vals:
                map[(from_x, y)] += 1
        elif from_x != to_x and from_y == to_y:
            min_val = min(from_x, to_x)
            max_val = max(from_x, to_x)
            vals = list(range(min_val, max_val + 1))
            for x in vals:
                map[(x, from_y)] += 1

    count = 0
    for coords, value in map.items():
        if value >= 2:
            count += 1

    return count


def part_b(data):
    data_lines = data.split('\n')
    lines = []
    for data_line in data_lines:
        left, _, right = data_line.split(' ')
        from_x, from_y = left.split(',')
        to_x, to_y = right.split(',')
        lines.append([[int(from_x), int(from_y)], [int(to_x), int(to_y)]])

    map = defaultdict(lambda: 0)

    def get_gen(from_val, to_val):
        if from_val == to_val:
            return [from_val for _ in range(10000)]
        if from_val > to_val:
            return range(from_val, to_val - 1, -1)
        else:
            return range(from_val, to_val + 1)

    for from_c, to_c in lines:
        from_x, from_y = from_c
        to_x, to_y = to_c

        x_gen = get_gen(from_x, to_x)
        y_gen = get_gen(from_y, to_y)

        points = [(x, y) for x, y in zip(x_gen, y_gen)]

        for coords in points:
            map[coords] += 1

    count = 0
    for coords, value in map.items():
        if value >= 2:
            count += 1

    return count


def main():
    data = get_data()

    #     data = """0,9 -> 5,9
    # 8,0 -> 0,8
    # 9,4 -> 3,4
    # 2,2 -> 2,1
    # 7,0 -> 7,4
    # 6,4 -> 2,0
    # 0,9 -> 2,9
    # 3,4 -> 1,4
    # 0,0 -> 8,8
    # 5,5 -> 8,2"""

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
