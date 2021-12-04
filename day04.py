from aocd import get_data, submit


def calc_score(board, seen_numbers):
    last_number = seen_numbers[-1]
    sum = 0
    for line in board:
        for number in line:
            if number not in seen_numbers:
                sum += number
    return sum * last_number


def part_a(data):
    lines = data.strip().split('\n')
    numbers = [int(x) for x in lines[0].split(',')]
    boards = []
    board = []
    for line in lines[2:]:
        if line == '':
            boards.append(board)
            board = []
            continue
        board_line = []
        for x in line.split(' '):
            if x == '':
                continue
            board_line.append(int(x))
        board.append(board_line)
    boards.append(board)

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
    lines = data.strip().split('\n')
    numbers = [int(x) for x in lines[0].split(',')]
    boards = []
    board = []
    for line in lines[2:]:
        if line == '':
            boards.append(board)
            board = []
            continue
        board_line = []
        for x in line.split(' '):
            if x == '':
                continue
            board_line.append(int(x))
        board.append(board_line)
    boards.append(board)

    board_idx_won = []

    for i in range(len(numbers)):
        seen_numbers = numbers[0:i]

        for board_idx, board in enumerate(boards):
            board_transposed = list(map(list, zip(*board)))
            won = False
            for line in board:
                if all([number in seen_numbers for number in line]):
                    won = True
            for line in board_transposed:
                if all([number in seen_numbers for number in line]):
                    won = True

            if won:
                if board_idx not in board_idx_won:
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
