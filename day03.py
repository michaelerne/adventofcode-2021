from collections import defaultdict, Counter

from aocd import get_data, submit


def part_a(data):
    lines = data.split('\n')

    bits = defaultdict(Counter)
    for line in lines:
        for index, bit in enumerate([int(x) for x in line]):
            bits[index][bit] += 1

    gamma = 0

    gamma_str = ''
    epsilon = 0
    epsilon_str = ''
    for index, counter in bits.items():
        if counter[0] > counter[1]:
            most_common = 0
            least_common = 1
        else:
            most_common = 1
            least_common = 0

        gamma += most_common * 2 ** index
        gamma_str += str(most_common)
        epsilon += least_common * 2 ** index
        epsilon_str += str(least_common)

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)
    return gamma * epsilon


def part_b(data):
    lines = data.split('\n')

    oxy = lines.copy()
    co2 = lines.copy()

    lst = oxy
    i = 0
    while len(lst) > 1:
        most_common = Counter()
        for line in lst:
            most_common[line[i]] += 1

        if most_common['1'] >= most_common['0']:
            most_common = '1'
        else:
            most_common = '0'

        new_lst = []
        for line in lst:
            if line[i] == most_common:
                new_lst.append(line)

        lst = new_lst
        i += 1
    oxy = int(lst[0], 2)


    lst = co2
    i = 0
    while len(lst) > 1:
        most_common = Counter()
        for line in lst:
            most_common[line[i]] += 1

        if most_common['1'] < most_common['0']:
            most_common = '1'
        else:
            most_common = '0'

        new_lst = []
        for line in lst:
            if line[i] == most_common:
                new_lst.append(line)

        lst = new_lst
        i += 1
    co2 = int(lst[0], 2)

    res = oxy * co2
    return res


def main():
    data = get_data()

#     data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
