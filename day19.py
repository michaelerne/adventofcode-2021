import itertools as it
import time

import parse
from aocd import get_data


def get_scanners(data):
    scanners = data.split('\n\n')

    return [[(x, y, z) for x, y, z in parse.findall('{:d},{:d},{:d}', scanner)] for scanner in scanners]


POS_POSITIVE = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
SIGN_POSITIVE = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1)]
POS_NEGATIVE = [(0, 2, 1), (1, 0, 2), (2, 1, 0)]
SIGN_NEGATIVE = [(-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, -1)]
PERM_24 = list(it.chain(it.product(POS_POSITIVE, SIGN_POSITIVE), it.product(POS_NEGATIVE, SIGN_NEGATIVE)))


def scanner_permutations(scanner):
    for (x_pos, y_pos, z_pos), (x_sign, y_sign, z_sign) in PERM_24:
        yield [(pos[x_pos] * x_sign, pos[y_pos] * y_sign, pos[z_pos] * z_sign) for pos in scanner]


def try_merge(scanner_a, scanner_b):
    a_set = set(scanner_a)

    for b in scanner_permutations(scanner_b):
        for a_pos in scanner_a:
            for b_pos in b:
                offset = [b_pos[0] - a_pos[0], b_pos[1] - a_pos[1], b_pos[2] - a_pos[2]]
                b_set = {(b_pos2[0] - offset[0], b_pos2[1] - offset[1], b_pos2[2] - offset[2]) for b_pos2 in b}
                matches = len(a_set & b_set)
                if matches >= 12:
                    return True, list(a_set | b_set), offset
    return False, None, None


def part_a(data):
    scanners = get_scanners(data)

    aligned_idx = 0
    unaligned_idx = {*list(range(1, len(scanners)))}

    next_idx = len(scanners)

    while unaligned_idx:
        for s2_idx in unaligned_idx:
            success, s3, _ = try_merge(scanners[aligned_idx], scanners[s2_idx])
            if success:
                unaligned_idx.remove(s2_idx)
                scanners.append(s3)
                aligned_idx = next_idx
                next_idx += 1
                break

    return len(scanners[-1])


def part_b(data):
    scanners = get_scanners(data)

    aligned_idx = 0
    unaligned_idx = {*list(range(1, len(scanners)))}

    next_idx = len(scanners)

    positions = [(0, 0, 0)]

    while unaligned_idx:
        for s2_idx in unaligned_idx:
            success, s3, s2_pos = try_merge(scanners[aligned_idx], scanners[s2_idx])
            if success:
                unaligned_idx.remove(s2_idx)
                scanners.append(s3)
                aligned_idx = next_idx
                positions.append(s2_pos)
                next_idx += 1
                break

    distances = []
    for a, b in it.permutations(positions, 2):
        distances.append(sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])]))

    return max(distances)


def main():
    data = get_data()

    example_data = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
    example_solution_a = 79
    example_solution_b = 3621

    # example_answer_a = part_a(example_data)
    # assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

    # answer_a = part_a(data)
    # submit(answer=answer_a, part="a")

    start = time.perf_counter_ns()
    example_answer_b = part_b(example_data)
    end = time.perf_counter_ns()
    assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    # answer_b = part_b(data)
    # submit(answer=answer_b, part="b")

    print(f"duration: {(end - start) / 1E6} ms")


if __name__ == '__main__':
    main()
