from collections import defaultdict, deque

from run_util import run_puzzle


def get_graph(data):
    graph = defaultdict(set)
    for k, v in [line.split('-') for line in data.split('\n')]:
        graph[k].add(v)
        graph[v].add(k)
    return graph


def bfs(graph, path, small_caves_visited, allow_one_multi_visit=False):
    cave = path[-1]
    if cave == "end":
        return [path]

    paths_found = []
    for neighbor in graph[cave]:
        if neighbor not in small_caves_visited:
            paths_found += bfs(
                graph,
                path + [neighbor],
                small_caves_visited | ({neighbor} if neighbor.islower() else set()),
                allow_one_multi_visit
            )
        elif allow_one_multi_visit and neighbor != "start":
            paths_found += bfs(
                graph,
                path + [neighbor],
                small_caves_visited,
                False
            )

    return paths_found


def part_a(data):
    graph = get_graph(data)

    start = (['start'], {'start'})
    paths = []
    queue = deque([start])
    while queue:
        path, small_caves_visited = queue.popleft()
        cave = path[-1]
        if cave == 'end':
            paths.append(path)
            continue
        for neighbor in graph[cave]:
            if neighbor not in small_caves_visited:
                queue.append((
                    path + [neighbor],
                    small_caves_visited | ({neighbor} if neighbor.islower() else set())
                ))
    return len(paths)


def part_a_rec(data):
    graph = get_graph(data)
    paths = bfs(graph, ['start'], {'start'}, False)
    return len(paths)


def part_b(data):
    graph = get_graph(data)

    start = (['start'], {'start'}, True)
    paths = []
    queue = deque([start])
    while queue:
        path, small_caves_visited, allow_one_multi_visit = queue.popleft()
        cave = path[-1]
        if cave == 'end':
            paths.append(path)
            continue
        for neighbor in graph[cave]:
            if neighbor not in small_caves_visited:
                queue.append((
                    path + [neighbor],
                    small_caves_visited | ({neighbor} if neighbor.islower() else set()),
                    allow_one_multi_visit
                ))
            elif allow_one_multi_visit and neighbor != "start":
                queue.append((
                    path + [neighbor],
                    small_caves_visited,
                    False
                ))
    return len(paths)


def part_b_rec(data):
    graph = get_graph(data)
    paths = bfs(graph, ['start'], {'start'}, True)
    return len(paths)


def main():
    examples = [
        ("""start-A
start-b
A-c
A-b
b-d
A-end
b-end""", 10, 36),
        ("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""", 19, 103),
        ("""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""", 226, 3509)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
