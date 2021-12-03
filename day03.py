from collections import Counter
from math import ceil

from aocd import get_data, submit
from typing import List, Callable

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

    matrix = [[int(x) for x in line] for line in lines]

    def rec(matrix: List[List[int]], index: int, bits: str, comparator: Callable[[int, int], bool]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        majority = ceil(len(matrix) / 2)

        transposed = list(map(list, zip(*matrix)))

        most_common = 1 if sum([x for x in transposed[index]]) >= majority else 0
        matrix = [row for row in matrix if comparator(most_common, row[index])]
        index += 1
        return rec(matrix, index, bits, comparator)

    oxy_bits = rec(matrix, 0, '', lambda most_common, bit: most_common == bit)
    co2_bits = rec(matrix, 0, '', lambda most_common, bit: most_common != bit)
    oxy = int(''.join([str(x) for x in oxy_bits]), 2)
    co2 = int(''.join([str(x) for x in co2_bits]), 2)

    return oxy * co2


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
