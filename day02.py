from run_util import run_puzzle


def part_a(data):
    lines = data.split('\n')
    instructions = [line.split(' ') for line in lines]
    instructions = [(x, int(y)) for x, y in instructions]

    depth = 0
    horizontal = 0

    for instruction, amount in instructions:
        match instruction:
            case "forward":
                horizontal += amount
            case "down":
                depth += amount
            case "up":
                depth -= amount

    return depth * horizontal


def part_b(data):
    lines = data.split('\n')
    instructions = [line.split(' ') for line in lines]
    instructions = [(x, int(y)) for x, y in instructions]

    aim = 0
    depth = 0
    horizontal = 0

    for instruction, amount in instructions:
        match instruction:
            case "forward":
                horizontal += amount
                depth += aim * amount
            case "down":
                aim += amount
            case "up":
                aim -= amount

    return depth * horizontal


def main():
    examples = [
        ("""forward 5
down 5
forward 8
up 3
down 8
forward 2""", 150, 900)
    ]

    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
