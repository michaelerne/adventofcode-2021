from run_util import run_puzzle


def get_pairs(data):
    lines = data.split('\n')
    pairs = [(int(lines[i * 18 + 5][6:]), int(lines[i * 18 + 15][6:])) for i in range(14)]
    return pairs


def get_links(pairs):
    stack = []
    links = {}

    for i, (x_add, y_add) in enumerate(pairs):
        if x_add > 0:
            stack.append((i, y_add))
        else:
            j, y_add_2 = stack.pop()
            links[i] = (j, y_add_2 + x_add)

    return links


def part_a(data):
    pairs = get_pairs(data)
    links = get_links(pairs)

    assignments = {}

    for i, (j, delta) in links.items():
        assignments[i] = min(9, 9 + delta)
        assignments[j] = min(9, 9 - delta)

    answer = int("".join(str(assignments[x]) for x in range(14)))

    return answer


def part_b(data):
    pairs = get_pairs(data)
    links = get_links(pairs)

    assignments = {}

    for i, (j, delta) in links.items():
        assignments[i] = max(1, 1 + delta)
        assignments[j] = max(1, 1 - delta)

    answer = int("".join(str(assignments[x]) for x in range(14)))

    return answer


def main():
    examples = []
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
