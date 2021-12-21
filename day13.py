from run_util import run_puzzle


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
        return ';'.join([f'{x},{y}' for x, y in sorted(points)])

    max_x = max([x for x, _ in points]) + 1

    lookup = {
        '0,1;0,2;0,3;0,4;0,5;1,0;1,3;2,0;2,3;3,1;3,2;3,3;3,4;3,5': 'A',
        '0,1;0,2;0,3;0,4;1,0;1,5;2,0;2,5;3,1;3,4': 'C',
        '0,0;0,1;0,2;0,3;0,4;0,5;1,0;1,2;1,5;2,0;2,2;2,5;3,0;3,5': 'E',
        '0,1;0,2;0,3;0,4;1,0;1,5;2,0;2,3;2,5;3,1;3,3;3,4;3,5': 'G',
        '0,1;1,2;0,4;3,4;0,0;3,1;0,3;3,0;0,2;3,3;0,5;2,2;3,2;3,5': 'H',
        '0,4;1,5;2,0;2,5;3,0;3,1;3,2;3,3;3,4': 'J',
        '0,1;2,4;1,2;0,4;2,1;0,0;0,3;3,0;2,3;0,2;0,5;3,5': 'K',
        '0,0;0,1;0,2;0,3;0,4;0,5;1,5;2,5;3,5': 'L',
        '0,0;0,1;0,2;0,3;0,4;0,5;1,0;1,3;2,0;2,3;3,1;3,2': 'P',
        '0,0;0,1;0,2;0,3;0,4;0,5;1,0;1,3;2,0;2,3;2,4;3,1;3,2;3,5': 'R',
        '0,0;0,1;0,2;0,3;0,4;1,5;2,5;3,0;3,1;3,2;3,3;3,4': 'U',
        '0,0;0,4;0,5;1,0;1,3;1,5;2,0;2,2;2,5;3,0;3,1;3,5': 'Z',
        '0,0;0,1;0,2;0,3;0,4;1,0;1,4;2,0;2,4;3,0;3,4;4,0;4,1;4,2;4,3;4,4': 'O',
    }
    for x_gap in range(max_x // 5 + 1):
        char_points = set()
        for x, y in points:
            if x_gap * 5 <= x <= (x_gap * 5) + 4:
                char_points.add((x, y))
        points -= char_points
        char_points = {(x - x_gap * 5, y) for x, y in char_points}

        index = hash(char_points)
        if index:
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
    examples = [
        ("""6,10
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
fold along x=5""", 17, 'O')
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
