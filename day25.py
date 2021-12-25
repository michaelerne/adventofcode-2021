from run_util import run_puzzle


def parse_data(data):
    lines = data.split('\n')
    eastbound = set()
    southbound = set()
    for y, line in enumerate(lines):
        for x, pos in enumerate(line):
            if pos == '.':
                continue
            if pos == '>':
                eastbound.add((x, y))
            elif pos == 'v':
                southbound.add((x, y))

    y_max = len(lines)
    x_max = len(lines[0])
    return eastbound, southbound, x_max, y_max


def print_grid(step, eastbound, southbound, x_max, y_max):
    lines = []
    print()
    print(f'After step {step}:')
    for y in range(y_max):
        line = ''
        for x in range(x_max):
            point = (x, y)
            if point in eastbound:
                line += '>'
            elif point in southbound:
                line += 'v'
            else:
                line += '.'
        lines.append(line)

    print('\n'.join(lines))


def part_a(data):
    eastbound, southbound, x_max, y_max = parse_data(data)

    step = 0

    while True:
        # print_grid(step, eastbound, southbound, x_max, y_max)

        step += 1
        moved = 0

        combined = eastbound | southbound

        new_eastbound = set()
        for old_loc in eastbound:
            new_loc = ((old_loc[0] + 1) % x_max, old_loc[1])
            if new_loc not in combined:
                new_eastbound.add(new_loc)
                moved += 1
            else:
                new_eastbound.add(old_loc)

        combined = new_eastbound | southbound

        new_southbound = set()
        for old_loc in southbound:
            new_loc = (old_loc[0], (old_loc[1] + 1) % y_max)
            if new_loc not in combined:
                new_southbound.add(new_loc)
                moved += 1
            else:
                new_southbound.add(old_loc)

        eastbound, southbound = new_eastbound, new_southbound

        if moved == 0:
            break

    return step


def main():
    examples = [
        ("""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""", 58, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, None, examples)


if __name__ == '__main__':
    main()
