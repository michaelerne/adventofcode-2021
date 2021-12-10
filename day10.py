from aocd import get_data, submit
import parse


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

    return sorted(scores)[len(scores)//2]


def main():
    data = get_data()

    example_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    example_solution_a = 26397
    example_solution_b = 288957

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
