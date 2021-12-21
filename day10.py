from run_util import run_puzzle

chunk_delims = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part_a(data):
    lines = data.split('\n')

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in chunk_delims.keys():
                stack.append(char)
            else:
                if char == chunk_delims[stack[-1]]:
                    stack.pop()
                else:
                    score += points[char]
                    break

    return score


def part_b(data):
    lines = data.split('\n')
    scores = []
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    for line in lines:
        stack = []
        corrupted = False
        for char in line:
            if char in chunk_delims.keys():
                stack.append(char)
            else:
                if char == chunk_delims[stack[-1]]:
                    stack.pop()
                else:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            for char in reversed(stack):
                score *= 5
                score += points[chunk_delims[char]]

            scores.append(score)

    return sorted(scores)[len(scores) // 2]


def part_a_stackless(data):
    lines = data.splitlines()

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    pairs = ['()', '[]', '{}', '<>']
    score = 0

    for line in lines:

        while sum([line.count(pair) for pair in pairs]):
            for pair in pairs:
                line = line.replace(pair, '')

        corruption = {
            token: line.index(token)
            for token in chunk_delims.values()
            if token in line
        }

        if corruption:
            first_corruption = min(corruption, key=corruption.get)
            score += points[first_corruption]

    return score


def part_b_stackless(data):
    lines = data.splitlines()

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    pairs = ['()', '[]', '{}', '<>']
    scores = []
    for line in lines:

        while sum([line.count(pair) for pair in pairs]):
            for pair in pairs:
                line = line.replace(pair, '')

        corrupted = any([token in line for token in chunk_delims.values()])
        if not corrupted:
            score = 0
            for char in reversed(line):
                score *= 5
                score += points[chunk_delims[char]]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    examples = [
        ("""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""", 26397, 288957)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)
    run_puzzle(day, part_a_stackless, part_b_stackless, examples)


if __name__ == '__main__':
    main()
