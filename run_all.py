import importlib
import time

from aocd import get_data, submit
from tqdm import tqdm

days_solved = 25


def main():
    timings = {}
    for day in tqdm(range(1, days_solved + 1), desc="Solving AoC2021", unit="day"):
        if day == 19:
            continue
        d = importlib.import_module(f'day{str(day).zfill(2)}')

        data = get_data(day=day)

        start = time.perf_counter_ns()
        answer_a = d.part_a(data)
        end = time.perf_counter_ns()
        timings[f'day{str(day).zfill(2)}_a'] = end - start
        submit(answer_a, day=day, part='a', quiet=True, reopen=False)

        if day != 25:
            start = time.perf_counter_ns()
            answer_b = d.part_b(data)
            end = time.perf_counter_ns()
            timings[f'day{str(day).zfill(2)}_b'] = end - start
            submit(answer_b, day=day, part='b', quiet=True, reopen=False)

    print()
    print("timings:")
    total = 0
    for title, duration_ns in timings.items():
        print(f'{title}: {duration_ns / 1E6} ms')
        total += duration_ns
    print(f'total: {total / 1E6} ms')


if __name__ == '__main__':
    main()
