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

def part_a(data):
    numbers, boards = parse_data(data)

    for i in range(len(numbers)):
        seen_numbers = numbers[0:i]
        for board in boards:
            board_transposed = list(map(list, zip(*board)))
            for line in board:
                if all([number in seen_numbers for number in line]):
                    return calc_score(board, seen_numbers)
            for line in board_transposed:
                if all([number in seen_numbers for number in line]):
                    return calc_score(board, seen_numbers)


def part_b(data):
    numbers, boards = parse_data(data)

    board_idx_won = []

    for i in range(len(numbers)):
        seen_numbers = numbers[0:i]

        for board_idx, board in enumerate(boards):

            if board_idx in board_idx_won:
                continue

            board_transposed = list(map(list, zip(*board)))
            won = False
            for line in board:
                if all([number in seen_numbers for number in line]):
                    won = True
            for line in board_transposed:
                if all([number in seen_numbers for number in line]):
                    won = True

            if won:
                if len(boards) - len(board_idx_won) == 1:
                    return calc_score(board, seen_numbers)

                board_idx_won.append(board_idx)


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
