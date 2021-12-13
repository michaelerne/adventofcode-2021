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


def do_fold(points, axis, index):
    if axis == 'x':
        return {(min(x, 2 * index - x), y) for x, y in points}
    else:
        return {(x, min(y, 2 * index - y)) for x, y in points}


def part_a(data):
    points, folds = parse_data(data)

    axis, index = folds[0]

    points = do_fold(points, axis, index)

    return len(points)


def points_to_text(points):

    text = ''

    def hash(points):
        return ';'.join([f'{x},{y}' for x, y in points])

    max_x = max([x for x, _ in points]) + 1

    lookup = {
        '0,1;1,2;0,4;1,5;0,0;0,3;2,0;3,0;0,2;0,5;2,2;1,0;2,5;3,5': 'E',
        '0,1;0,4;0,0;3,1;0,3;2,0;2,3;0,2;0,5;1,0;3,2;1,3': 'P',
        '0,1;0,4;1,5;0,0;0,3;0,2;0,5;2,5;3,5': 'L',
        '0,1;0,4;3,4;1,5;3,1;0,3;2,0;2,3;0,2;3,3;1,0;2,5;3,5': 'G',
        '0,1;2,4;0,4;0,0;3,1;0,3;2,0;2,3;0,2;0,5;1,0;3,2;1,3;3,5': 'R',
        '0,1;0,4;3,4;0,0;3,1;1,5;0,3;3,0;0,2;3,3;3,2;2,5': 'U',
        '0,1;0,4;0,0;1,5;0,3;0,2;0,5;2,5;3,5': 'L',
    }
    for x_gap in range(max_x // 5 + 1):
        char_points = set()
        for x, y in points:
            if x_gap * 5 <= x <= (x_gap * 5) + 4:
                char_points.add((x, y))
        points -= char_points
        char_points = {(x - x_gap * 5, y) for x, y in char_points}

        index = hash(char_points)
        if index not in lookup:
            print("Missing entry:\n")
            print_points(char_points)
            letter = input('Which Character is this? ')
            print()
            print("please add the following line to the lookup dict:")
            letter_hash = hash(char_points)
            print(f"    '{letter_hash}': '{letter}',")
            lookup[letter_hash] = letter

        text += lookup[index]

    return text


def part_b(data):
    points, folds = parse_data(data)

    for axis, index in folds:
        points = do_fold(points, axis, index)

    return points_to_text(points)


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

    # example_answer_b = part_b(example_data)
    # assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
