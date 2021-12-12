from collections import defaultdict, deque

from aocd import get_data, submit


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
    data = get_data()

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

    for example_data, example_solution_a, example_solution_b in examples:
        example_answer_a = part_a(example_data)
        assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    for example_data, example_solution_a, example_solution_b in examples:
        example_answer_b = part_b(example_data)
        assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
