from collections import Counter

from aocd import get_data, submit


def parse_data2(data):
    lines = data.split('\n')
    template = Counter(zip(lines[0], lines[0][1:]))
    mappings = dict()
    for line in lines[2:]:
        tokens = line.split(' -> ')
        mappings[(tokens[0][0], tokens[0][1])] = [(tokens[0][0], tokens[1]), (tokens[1], tokens[0][1])]

    return template, mappings, lines[0]


def do_step(template, mappings):
    new_template = Counter()
    for source, destinations in mappings.items():
        if source in template:
            for destination in destinations:
                new_template[destination] += template[source]
    return new_template


def part_a(data):
    template, mappings, initial_template_string = parse_data2(data)

    for step in range(10):
        template = do_step(template, mappings)

    return get_answer(template, initial_template_string)


def get_answer(template, initial_template_string):
    counter = Counter()
    for x, count in template.items():
        counter[x[0]] += count
        counter[x[1]] += count
    counter[initial_template_string[0]] += 1
    counter[initial_template_string[-1]] += 1

    most = counter.most_common()[0][1]
    least = counter.most_common()[-1][1]
    return (most - least) // 2


def part_b(data):
    template, mappings, initial_template_string = parse_data2(data)

    for step in range(40):
        template = do_step(template, mappings)

    return get_answer(template, initial_template_string)


def main():
    data = get_data()

    example_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    example_solution_a = 1588
    example_solution_b = 2188189693529

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
