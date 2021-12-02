from aocd import get_data, submit


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
            case "up": depth -= amount


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
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
