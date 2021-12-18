from aocd import get_data, submit
import parse


def part_a(data):
    input = [int(x) for x in data.split(',')]
    return 0


def part_b(data):
    input = [int(x) for x in data.split(',')]
    return 0


def main():
    data = get_data()

    example_data = """"""
    example_solution_a = 1
    example_solution_b = 1

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