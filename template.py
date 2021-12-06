from aocd import get_data, submit
import parse


def part_a(data):
    return ''


def part_b(data):
    return ''


def main():
    data = get_data()

    example_data = """"""
    example_solution_a = None
    example_solution_b = None

    example_answer_a = part_a(example_data)
    assert example_answer_a == example_solution_a, "example_data did not match for part_a"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b == example_solution_b, "example_data did not match for part_b"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
