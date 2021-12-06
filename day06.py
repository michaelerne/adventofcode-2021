from aocd import get_data, submit
import parse


def part_a(data):
    return ''


def part_b(data):
    return ''


def main():
    data = get_data()

    example_data = """"""

    example_answer_a = part_a(example_data)
    assert example_answer_a, None

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    example_answer_b = part_b(example_data)
    assert example_answer_b, None

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
