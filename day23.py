import heapq

from run_util import run_puzzle

WAITING_ROW = 1
WAITING_COLS = [1, 2, 4, 6, 8, 10, 11]
ROOM_COLS = [3, 5, 7, 9]
COST = {"A": 1, "B": 10, "C": 100, "D": 1000}


def parse_data(data):
    waitings = tuple('.' for _ in WAITING_COLS)
    rooms = ([], [], [], [])

    for line in data.split('\n')[2:]:
        if '#########' in line:
            continue
        line = line.replace('#', '').replace(' ', '')
        for room_idx, pod in enumerate(line):
            rooms[room_idx].append(pod)
    rooms = tuple(tuple(room) for room in rooms)

    return waitings, rooms


def manhattan_distance(x, y):
    return sum([abs(a - b) for a, b in zip(x, y)])


def dijkstra(initial_board, get_boards, target_board):
    seen = set()
    costs = {initial_board: 0}

    # ideas: having the data as lists instead of tuples would be easier to find boards
    #        but we cannot hash lists. should we create a small hash fn?
    todo = [(0, initial_board)]

    while todo:
        cost, board = heapq.heappop(todo)

        if board in seen:
            continue

        if board == target_board:
            return cost

        seen.add(board)

        for diff_costs, new_board in get_boards(board):
            new_costs = cost + diff_costs
            if new_board not in costs or new_costs < costs[new_board]:
                heapq.heappush(todo, (new_costs, new_board))


def solve(hallway, rooms):
    def get_boards(current_board):
        out = []

        current_waitings, current_rooms = current_board

        def is_blocked(col_1, col_2):
            low, high = min(col_1, col_2), max(col_1, col_2)
            return any([
                current_waitings[WAITING_COLS.index(col)]
                for col in range(low + 1, high)
                if col in WAITING_COLS and current_waitings[WAITING_COLS.index(col)] != "."
            ])

        # room -> waiting spot
        for room_idx, room in enumerate(current_rooms):
            occupied_positions = [room_pos for room_pos, pos in enumerate(room) if pos != '.']
            if not occupied_positions:
                continue
            room_position = min(occupied_positions)
            to_move_row, to_move = 2 + room_position, room[room_position]

            for waiting_idx, waiting_col in enumerate(WAITING_COLS):
                if current_waitings[waiting_idx] == ".":
                    if is_blocked(waiting_col, ROOM_COLS[room_idx]):
                        continue

                    cost = manhattan_distance((to_move_row, ROOM_COLS[room_idx]), (WAITING_ROW, waiting_col)) * COST[to_move]

                    new_waitings = list(current_waitings)
                    new_rooms = list(map(list, current_rooms))

                    new_waitings[waiting_idx] = to_move
                    new_rooms[room_idx][room_position] = "."

                    out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        # waiting spot -> room
        for waiting_idx, waiting_col in enumerate(WAITING_COLS):
            to_move = current_waitings[waiting_idx]
            if to_move == ".":
                continue

            target_room_idx = ord(to_move) - ord('A')
            target_room = current_rooms[target_room_idx]

            if target_room[0] == "." and all(x == "." or x == to_move for x in target_room[1:]):
                free_positions = [room_pos for room_pos, pos in enumerate(target_room) if pos == '.']
                room_position = max(free_positions)
                room_row = room_position + 2

                room_col = ROOM_COLS[target_room_idx]
                if is_blocked(waiting_col, room_col):
                    continue

                cost = manhattan_distance((room_row, room_col), (WAITING_ROW, waiting_col)) * COST[to_move]

                new_waitings = list(current_waitings)
                new_rooms = list(map(list, current_rooms))

                new_waitings[waiting_idx] = "."
                new_rooms[target_room_idx][room_position] = to_move

                out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        return out

    initial_board = (hallway, rooms)
    target_board = (hallway, tuple((chr(ord('A') + i),) * len(rooms[0]) for i, _ in enumerate(rooms)))
    cost = dijkstra(initial_board=initial_board, target_board=target_board, get_boards=get_boards)
    return cost


def part_a(data):
    hallway, rooms = parse_data(data)

    answer = solve(hallway, rooms)

    return answer


def part_b(data):
    lines = data.split('\n')
    data = '\n'.join(
        lines[0:3] +
        [
            "  #D#C#B#A#",
            "  #D#B#A#C#"
        ] +
        lines[3:]
    )

    hallway, rooms = parse_data(data)

    answer = solve(hallway, rooms)

    return answer


def main():
    examples = [
        ("""#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""", 12521, 44169)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, None, part_b, examples)


if __name__ == '__main__':
    main()
