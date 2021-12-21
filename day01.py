from run_util import run_puzzle


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
    examples = [
        ("""199
200
208
210
200
207
240
269
260
263""", 7, 5)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
