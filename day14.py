from collections import Counter

import parse
from aocd import get_data, submit


def parse_data2(data):
    template, mapping_strings = data.split('\n\n')
    pairs = Counter(zip(template, template[1:]))
    mappings = {
        (a, b): [(a, c), (c, b)]
        for a, b, c in parse.findall('{:l}{:l} -> {:l}', mapping_strings)
    }
    return pairs, mappings, template


def do_step(pairs, mappings):
    new_pairs = Counter()
    for source, destinations in mappings.items():
        if source in pairs:
            for destination in destinations:
                new_pairs[destination] += pairs[source]
    return new_pairs


def part_a(data):
    pairs, mappings, template = parse_data2(data)

    for step in range(10):
        pairs = do_step(pairs, mappings)

    return get_answer(pairs, template)


def get_answer(pairs, template):
    counter = Counter()
    for pair, count in pairs.items():
        counter[pair[0]] += count
        counter[pair[1]] += count
    counter[template[0]] += 1
    counter[template[-1]] += 1

    frequency = counter.most_common()
    most = frequency[0][1]
    least = frequency[-1][1]
    return (most - least) // 2


def part_b(data):
    pairs, mappings, template = parse_data2(data)

    for step in range(40):
        pairs = do_step(pairs, mappings)

    return get_answer(pairs, template)


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
