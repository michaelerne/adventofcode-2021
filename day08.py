import itertools

from aocd import get_data, submit


def part_a(data):
    number_lookup = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    digs = [1, 4, 7, 8]
    lens = [len(number_lookup[x]) for x in digs]
    lines = [x for x in data.split('\n')]

    signals = []
    outputs = []

    for line in lines:
        signal, output = line.split(' | ')
        signals.append(signal.split(' '))
        outputs.append(output.split(' '))
    i = 0
    for output in outputs:
        for o in output:
            if len(o) in lens:
                i += 1
    return i


def part_b(data):
    lines = [x for x in data.split('\n')]

    mapping = {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1
    }

    mapping = {
        "".join(sorted(k)): v
        for k, v in mapping.items()
    }

    answer = 0

    for line in lines:
        signal, output = line.split(' | ')
        signals = signal.split(' ')
        outputs = output.split(' ')

        for permutation in itertools.permutations("abcdefg"):
            scramble = {
                signals: outputs for signals, outputs
                in zip(permutation, "abcdefg")
            }

            scrambled_signals = ["".join(sorted(scramble[c] for c in signal)) for signal in signals]
            if all(scrambled_signal in mapping for scrambled_signal in scrambled_signals):
                scrambled_outputs = ["".join(sorted(scramble[c] for c in output)) for output in outputs]
                answer += int("".join(str(mapping[x]) for x in scrambled_outputs))
                break
    return answer


def main():
    data = get_data()

    example_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    example_solution_a = 26
    example_solution_b = 61229

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
