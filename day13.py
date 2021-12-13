from aocd import get_data, submit


def parse_data(data):
    lines = data.split('\n')
    points = set()
    folds = []
    for line in lines:
        if line == '':
            continue
        if line.startswith('fold'):
            _, _, instruction = line.split(' ')
            axis, index = instruction.split('=')
            folds.append((axis, int(index)))
        else:
            x, y = line.split(',')
            points.add((int(x), int(y)))

    return points, folds


def print_points(points):
    max_x = max([x for x, _ in points]) + 1
    max_y = max([y for _, y in points]) + 1

    for y in range(max_y):
        print(''.join(['#' if (x, y) in points else ' ' for x in range(max_x)]))


def do_fold(points, fold):
    axis, index = fold
    new_points = set()

    for x, y in points:

        if axis == 'x' and x > index:
            new_points.add((2 * index - x, y))
        elif axis == 'y' and y > index:
            new_points.add((x, 2 * index - y))
        else:
            new_points.add((x, y))

    return new_points


def part_a(data):
    points, folds = parse_data(data)

    points = do_fold(points, folds[0])

    return len(points)


def part_b(data):
    points, folds = parse_data(data)

    for fold in folds:
        points = do_fold(points, fold)

    print_points(points)
    answer = input("what do you read?")
    print()
    return answer


def main():
    data = get_data()

    example_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    example_solution_a = 17
    example_solution_b = '0'

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
