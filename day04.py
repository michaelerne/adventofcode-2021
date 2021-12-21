from run_util import run_puzzle


def calc_score(board, seen_numbers):
    last_number = seen_numbers[-1]
    sum_seen = sum([number for line in board for number in line if number not in seen_numbers])

    return sum_seen * last_number


def parse_data(data):
    lines = data.strip().split('\n')

    numbers = [int(x) for x in lines[0].split(",")]
    boards = [
        [[int(number) for number in line.split()] for line in board]
        for board in [lines[2 + x:2 + x + 5] for x in range(0, len(lines) - 1, 6)]
    ]

    return numbers, boards


def transpose(board):
    return list(map(list, zip(*board)))


def won(board, seen_numbers):
    return any([all([number in seen_numbers for number in line]) for line in board + transpose(board)])


def part_a(data):
    numbers, boards = parse_data(data)

    for i in range(len(numbers)):
        seen_numbers = numbers[0:i]
        for board in boards:
            if won(board, seen_numbers):
                return calc_score(board, seen_numbers)


def part_b(data):
    numbers, boards = parse_data(data)

    for i in range(len(numbers)):
        seen_numbers = numbers[0:i]

        remaining_boards = [
            board for board in boards
            if not won(board, seen_numbers)
        ]

        if not remaining_boards:
            return calc_score(boards[0], seen_numbers)
        else:
            boards = remaining_boards


def main():
    examples = [
        ("""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""", 4512, 1924)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
