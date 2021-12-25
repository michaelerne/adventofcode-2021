from collections import defaultdict
from itertools import combinations
from math import sqrt

from run_util import run_puzzle


def parse_data(data):
    scanners = [
        tuple(
            tuple(
                int(num)
                for num in scanner_line.split(',')
            )
            for scanner_line in scanner.split("\n")[1:])
        for scanner in data.split("\n\n")
    ]
    return scanners


def euclidean_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]

    return int(sqrt(dx ** 2 + dy ** 2 + dz ** 2))


def manhattan_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]

    return abs(dx) + abs(dy) + abs(dz)


def get_number_of_common_points(config_1, config_2):
    return max(
        [
            len(config_1[p0].intersection(config_2[p1]))
            for p0 in config_1
            for p1 in config_2
        ]
    )


def get_config(sensor_data):
    config = defaultdict(set)
    for p1 in sensor_data:
        for p2 in sensor_data:
            config[p1].add(euclidean_distance(p1, p2))
        config[p1].remove(0)

    return config


def align_configs(config1, config2):
    mapping = {}
    for p1 in config1:
        for p2 in config2:
            if len(config1[p1].intersection(config2[p2])) > 10:
                mapping[p1] = p2

    cog_1_x = sum([k[0] for k in mapping.keys()]) / len(mapping.keys())
    cog_1_y = sum([k[1] for k in mapping.keys()]) / len(mapping.keys())
    cog_1_z = sum([k[2] for k in mapping.keys()]) / len(mapping.keys())

    cog_2_x = sum([k[0] for k in mapping.values()]) / len(mapping.values())
    cog_2_y = sum([k[1] for k in mapping.values()]) / len(mapping.values())
    cog_2_z = sum([k[2] for k in mapping.values()]) / len(mapping.values())

    p1 = list(mapping.keys())[0]
    p2 = mapping[p1]

    p1_mod = (round(p1[0] - cog_1_x), round(p1[1] - cog_1_y), round(p1[2] - cog_1_z))
    p2_mod = (round(p2[0] - cog_2_x), round(p2[1] - cog_2_y), round(p2[2] - cog_2_z))

    rotation = {}
    for i in range(3):
        idx = list(map(abs, p2_mod)).index(abs(p1_mod[i]))
        rotation[i] = (idx, p1_mod[i] // p2_mod[idx])

    p2_rot = [0] * 3
    for i in range(3):
        p2_rot[i] = p2[rotation[i][0]] * rotation[i][1]

    translation = []
    for i in range(3):
        translation.append(p2_rot[i] - p1[i])

    return rotation, translation


def transform_points(rotation, translation, points):
    new_points = set()

    for point in points:
        new_points.add(
            tuple(
                point[rotation[i][0]] * rotation[i][1] - translation[i]
                for i in range(3)
            )
        )

    return new_points


def align_scanners(scanners):
    grid = set(scanners.pop(0))

    scanners_config = {scanner: get_config(scanner) for scanner in scanners}

    scanner_positions = []
    while len(scanners) > 0:
        grid_config = get_config(grid)
        scanners_common_points = [
            get_number_of_common_points(grid_config, scanners_config[scanner]) for scanner in scanners
        ]

        most_overlapping_scanner_idx = scanners_common_points.index(max(scanners_common_points))

        rotation, translation = align_configs(grid_config, scanners_config[scanners[most_overlapping_scanner_idx]])
        grid.update(transform_points(rotation, translation, scanners[most_overlapping_scanner_idx]))

        del scanners[most_overlapping_scanner_idx]
        scanner_positions.append(translation)

    return grid, scanner_positions


def part_a(data):
    scanners = parse_data(data)

    grid, scanner_positions = align_scanners(scanners)

    return len(grid)


def part_b(data):
    scanners = parse_data(data)

    grid, scanner_positions = align_scanners(scanners)

    return max([manhattan_distance(pos_1, pos_2) for pos_1, pos_2 in combinations(scanner_positions, 2)])


def main():
    examples = [
        ("""--- scanner 0 ---
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
30,-46,-14""", 79, 3621)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
