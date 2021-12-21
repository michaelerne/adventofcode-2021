import itertools

import parse

from run_util import run_puzzle


def parse_data(data):
    return [x.fixed[1] for x in parse.findall('Player {:d} starting position: {:d}', data)]


def deterministic_die():
    face = 1
    while True:
        yield face
        face += 1
        if face > 100:
            face = 1


def part_a(data):
    start = parse_data(data)

    die = deterministic_die()
    pos_1, pos_2, score_1, score_2 = start[0] - 1, start[1] - 1, 0, 0
    rolls = 0
    while True:
        pos_1 = (pos_1 + next(die) + next(die) + next(die)) % 10
        score_1 += pos_1 + 1
        rolls += 3

        if score_1 >= 1000:
            return score_2 * rolls

        pos_2 = (pos_2 + next(die) + next(die) + next(die)) % 10
        score_2 += pos_2 + 1
        rolls += 3

        if score_2 >= 1000:
            return score_1 * rolls


GAME_CACHE = {}
DIRAC_DIE = [1, 2, 3]


def play_game(pos_1, pos_2, score_1, score_2):
    if score_1 >= 21:
        return 1, 0
    if score_2 >= 21:
        return 0, 1
    if (pos_1, pos_2, score_1, score_2) in GAME_CACHE:
        return GAME_CACHE[(pos_1, pos_2, score_1, score_2)]
    ans = (0, 0)
    for die_1, die_2, die_3 in itertools.product(DIRAC_DIE, repeat=3):
        new_pos_1 = (pos_1 + die_1 + die_2 + die_3) % 10
        new_score_1 = score_1 + new_pos_1 + 1

        won_1, won_2 = play_game(pos_2, new_pos_1, score_2, new_score_1)
        ans = (ans[0] + won_2, ans[1] + won_1)
    GAME_CACHE[(pos_1, pos_2, score_1, score_2)] = ans
    return ans


def part_b(data):
    start = parse_data(data)
    return max(play_game(start[0] - 1, start[1] - 1, 0, 0))


def main():
    examples = [
        ("""Player 1 starting position: 4
Player 2 starting position: 8""", 739785, 444356092776315)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
