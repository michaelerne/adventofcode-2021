from math import ceil
from typing import List, Callable

from aocd import get_data, submit


def binary_to_decimal(input: List[int]) -> int:
    dec = 0
    for bit in input:
        dec = dec << 1 | bit
    return dec


def part_a(data):
    lines = data.split('\n')
    matrix = [[int(x) for x in line] for line in lines]
    transposed = list(map(list, zip(*matrix)))

    majority = ceil(len(matrix) / 2)

    gamma_str = ''.join(['1' if sum(column) >= majority else '0' for column in transposed])

    gamma = int(gamma_str, 2)

    epsilon = gamma ^ int(''.join(['1' for _ in range(len(gamma_str))]), 2)

    return gamma * epsilon


def part_b(data):
    lines = data.split('\n')

    def solve(matrix: List[List[int]], comparator: Callable[[int, int], bool]) -> int:
        index: int = 0
        while len(matrix) > 1:
            majority = ceil(len(matrix) / 2)

            transposed = list(map(list, zip(*matrix)))

            most_common = 1 if sum([x for x in transposed[index]]) >= majority else 0
            matrix = [row for row in matrix if comparator(most_common, row[index])]
            index += 1

        return binary_to_decimal(matrix[0])

    matrix = [[int(x) for x in line] for line in lines]

    oxy = solve(matrix, lambda most_common, bit: most_common == bit)
    co2 = solve(matrix, lambda most_common, bit: most_common != bit)

    return oxy * co2


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
