import itertools
import math
from functools import reduce

from aocd import get_data, submit


def parse_data(data):
    return [eval(line) for line in data.split('\n')]


def add_left(value, to_add):
    """
    >>> add_left(1, None)
    1
    >>> add_left(1, 1)
    2
    >>> add_left([1, 1], None)
    [1, 1]
    >>> add_left([1, 1], 1)
    [2, 1]
    >>> add_left([[1, 1], 1], None)
    [[1, 1], 1]
    >>> add_left([[1, 1], 1], 1)
    [[2, 1], 1]
    """
    if to_add is None:
        return value
    if isinstance(value, int):
        return value + to_add
    return [add_left(value[0], to_add), value[1]]


def add_right(value, to_add):
    """
    >>> add_right(1, None)
    1
    >>> add_right(1, 1)
    2
    >>> add_right([1, 1], None)
    [1, 1]
    >>> add_right([1, 1], 1)
    [1, 2]
    >>> add_right([1, [1, 1]], None)
    [1, [1, 1]]
    >>> add_right([1, [1, 1]], 1)
    [1, [1, 2]]
    """
    if to_add is None:
        return value
    if isinstance(value, int):
        return value + to_add
    return [value[0], add_right(value[1], to_add)]


def explode(value, depth_left=4):
    """
    >>> explode([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]])
    (True, None, [[[[0, 7], 4], [15, [0, 13]]], [1, 1]], None)
    >>> explode([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]])
    (True, None, [[[[0, 7], 4], [15, [0, 13]]], [1, 1]], None)
    >>> explode([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    (True, None, [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], None)
    >>> explode([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
    (False, None, [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], None)
    """
    if isinstance(value, int):
        return False, None, value, None
    if depth_left == 0:
        return True, value[0], 0, value[1]

    left, right = value

    # explode left
    exploded, left_add, left, right_add = explode(left, depth_left - 1)
    if exploded:
        return True, left_add, [left, add_left(right, right_add)], None

    # explode right
    exploded, left_add, right, right_add = explode(right, depth_left - 1)
    if exploded:
        return True, None, [add_right(left, left_add), right], right_add

    return False, None, value, None


def split(value):
    """
    >>> split([[[[0,7],4],[15,[0,13]]],[1,1]])
    (True, [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
    >>> split([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
    (True, [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]])
    >>> split([0, 0])
    (False, [0, 0])
    """
    if isinstance(value, int):
        if value >= 10:
            return True, [math.floor(value / 2), math.ceil(value / 2)]
        return False, value

    left, right = value

    change, left = split(left)
    if change:
        return True, [left, right]

    change, right = split(right)
    if change:
        return True, [left, right]

    return False, [left, right]


def add(left, right):
    """
    >>> add([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])
    [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    """
    value = [left, right]
    while True:
        change, _, value, _ = explode(value)
        if change:
            continue
        change, value = split(value)
        if not change:
            break
    return value


def magnitude(value):
    """
    >>> magnitude([[1,2],[[3,4],5]])
    143
    >>> magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    1384
    >>> magnitude([[[[1,1],[2,2]],[3,3]],[4,4]])
    445
    >>> magnitude([[[[3,0],[5,3]],[4,4]],[5,5]])
    791
    >>> magnitude([[[[5,0],[7,4]],[5,5]],[6,6]])
    1137
    >>> magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
    3488
    """
    if isinstance(value, int):
        return value
    return 3 * magnitude(value[0]) + 2 * magnitude(value[1])


def part_a(data):
    lines = parse_data(data)
    return magnitude(reduce(add, lines))


def part_b(data):
    lines = parse_data(data)
    return max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2))


def main():
    data = get_data()

    example_data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    example_solution_a = 4140
    example_solution_b = 3993

    example_answer_a = part_a(example_data)
    assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
