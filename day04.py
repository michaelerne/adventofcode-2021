from aocd import get_data, submit


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
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
