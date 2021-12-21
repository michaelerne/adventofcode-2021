from collections import Counter

import parse

from run_util import run_puzzle


def parse_data(data):
    template, mapping_strings = data.split('\n\n')
    pairs = Counter(zip(template, template[1:]))
    mappings = {
        (a, b): [(a, c), (c, b)]
        for a, b, c in parse.findall('{:l}{:l} -> {:l}', mapping_strings)
    }
    return pairs, mappings, template


def do_step(pairs, mappings):
    new_pairs = Counter()
    for source in pairs.keys():
        for destination in mappings[source]:
            new_pairs[destination] += pairs[source]
    return new_pairs


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


def part_a(data):
    pairs, mappings, template = parse_data(data)

    for step in range(10):
        pairs = do_step(pairs, mappings)

    return get_answer(pairs, template)


def part_b(data):
    pairs, mappings, template = parse_data(data)

    for step in range(40):
        pairs = do_step(pairs, mappings)

    return get_answer(pairs, template)


def main():
    examples = [
        ("""NNCB

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
CN -> C""", 1588, 2188189693529)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
