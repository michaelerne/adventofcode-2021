import datetime
import enum
import time
from typing import Dict, Set, List, Tuple

from aocd import get_data, submit


class Segment(enum.Enum):
    TOP = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3
    MIDDLE = 4
    BOTTOM_LEFT = 5
    BOTTOM_RIGHT = 6
    BOTTOM = 7


def get_mapping(signals):
    mapping: Dict[int, Set[str]] = {}
    segments: Dict[Segment, Set[str]] = {}

    for signal in signals:
        match len(signal):
            case 2:
                mapping[1] = signal
            case 3:
                mapping[7] = signal
            case 4:
                mapping[4] = signal
            case 7:
                mapping[8] = signal

    segments[Segment.TOP] = mapping[7] - mapping[4]
    mapping[3] = next(pattern for pattern in signals if len(pattern) == 5 and mapping[1] <= pattern)
    segments[Segment.TOP_LEFT] = mapping[4] - mapping[3]
    segments[Segment.MIDDLE] = mapping[4] - mapping[1] - segments[Segment.TOP_LEFT]
    segments[Segment.BOTTOM] = mapping[3] - mapping[4] - segments[Segment.TOP]

    mapping[0] = mapping[8] - segments[Segment.MIDDLE]
    segments[Segment.BOTTOM_LEFT] = mapping[0] - mapping[3] - segments[Segment.TOP_LEFT]

    mapping[5] = next(pattern for pattern in signals if len(pattern) == 5 and segments[Segment.TOP_LEFT] <= pattern)
    segments[Segment.TOP_RIGHT] = mapping[1] - mapping[5]
    segments[Segment.BOTTOM_RIGHT] = mapping[1] - segments[Segment.TOP_RIGHT]

    mapping[2] = mapping[3] - segments[Segment.BOTTOM_RIGHT] | segments[Segment.BOTTOM_LEFT]
    mapping[6] = mapping[5] | segments[Segment.BOTTOM_LEFT]
    mapping[9] = mapping[8] - segments[Segment.BOTTOM_LEFT]

    reverse_mapping = {
        ''.join(sorted(v)): str(k)
        for k, v in mapping.items()
    }

    return reverse_mapping


def parse_data(data) -> List[Tuple[List[Set[str]], List[str]]]:
    for line in data.split('\n'):
        left, right = line.split(' | ')
        signals = [set(signal) for signal in left.split()]
        outputs = [''.join(sorted(output)) for output in right.split()]
        yield signals, outputs


def part_a(data):
    answer = 0
    desired_lenghts = {2, 3, 4, 7}
    for _signals, outputs in parse_data(data):
        answer += sum([len(output) in desired_lenghts for output in outputs])
    return answer


def part_b(data):
    answer = 0
    for signals, outputs in parse_data(data):
        mapping = get_mapping(signals)
        answer += int(''.join([mapping[output] for output in outputs]))

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
