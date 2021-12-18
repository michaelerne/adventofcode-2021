import importlib

from aocd import get_data, submit


def main():
    for day in range(1, 18):
        mod = importlib.import_module(f'day{str(day).zfill(2)}')

        data = get_data(day=day)
        print(f"solving day {day}")
        answer_a = mod.part_a(data)
        answer_b = mod.part_b(data)
        print(f"submitting day {day}")
        submit(answer_a, day=day, part='a')
        submit(answer_b, day=day, part='b')


if __name__ == '__main__':
    main()
