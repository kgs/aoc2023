from collections import defaultdict
from typing import Callable


def check_symbol(i: int, j: int, engine_map: list[str], f: Callable[[str], bool]) -> (bool, tuple):
    for y in [j - 1, j, j + 1]:
        for x in [i - 1, i, i + 1]:
            if (x != i or y != j) and x >= 0 and y >= 0 and x < len(engine_map[0]) and y < len(engine_map):
                v = engine_map[y][x]
                if f(v):
                    return True, (x, y)
    return False, None


def sum_part_numbers(engine_map: list[str]) -> int:
    curr_number = ""
    should_add = False
    res = 0
    for j, row in enumerate(engine_map + ["." for _ in range(len(engine_map[0]))]):
        for i, e in enumerate(row + "."):
            if e.isdigit():
                if check_symbol(i, j, engine_map, lambda s: not s.isdigit() and s != '.'):
                    should_add = True
                curr_number += e
            else:
                if len(curr_number) > 0 and should_add:
                    res += int(curr_number)
                    should_add = False
                curr_number = ""
    return res


def sum_gears(engine_map: list[str]) -> int:
    curr_number = ""
    star_present = None
    res = 0
    possible_gears = defaultdict(list)
    for j, row in enumerate(engine_map + ["." for _ in range(len(engine_map[0]))]):
        for i, e in enumerate(row + "."):
            if e.isdigit():
                check, star_pos = check_symbol(i, j, engine_map, lambda s: s == '*')
                if check:
                    star_present = star_pos
                curr_number += e
            else:
                if len(curr_number) > 0 and star_present is not None:
                    possible_gears[star_present].append(int(curr_number))
                    star_present = None
                curr_number = ""
    for v in possible_gears.values():
        if len(v) == 2:
            res += v[0] * v[1]
    return res


def part1(input_txt: str) -> int:
    with open(input_txt) as f:
        engine_map = list(map(lambda x: x.strip(), f.readlines()))
        return sum_part_numbers(engine_map)


def part2(input_txt: str) -> int:
    with open(input_txt) as f:
        engine_map = list(map(lambda x: x.strip(), f.readlines()))
        return sum_gears(engine_map)


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
