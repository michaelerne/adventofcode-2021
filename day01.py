from aocd import get_data, submit


def part_a(data):
    measurements = [int(x) for x in data.split('\n')]

    increases = sum([1 for a, b in zip(measurements, measurements[1:]) if a < b])

    return increases


def part_b(data):
    measurements = [int(x) for x in data.split('\n')]

    measurements = [sum(x) for x in zip(measurements, measurements[1:], measurements[2:])]

    increases = sum([1 for a, b in zip(measurements, measurements[1:]) if a < b])

    return increases


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
