import re

R_MAX, G_MAX, B_MAX = 12, 13, 14


def parse_game_idx(game_str: str) -> int:
    if m := re.search(r"Game (\d+)", game_str):
        return int(m.group(1))


def parse_game_set(set_str: str) -> (int, int, int):
    r = g = b = 0
    if m := re.search(r"(\d+) red", set_str):
        r = int(m.group(1))
    if m := re.search(r"(\d+) green", set_str):
        g = int(m.group(1))
    if m := re.search(r"(\d+) blue", set_str):
        b = int(m.group(1))
    return r, g, b


def parse_game_sets(sets_str: str) -> list[(int, int, int)]:
    sets_list_str = sets_str.split(";")
    ret = []
    for set_str in sets_list_str:
        ret.append(parse_game_set(set_str))
    return ret


def parse_game(line: str) -> (int, list[(int, int, int)]):
    game_str, sets_str = line.split(":")
    idx = parse_game_idx(game_str)
    sets = parse_game_sets(sets_str)
    return idx, sets


def game_possible(sets: list[(int, int, int)]) -> bool:
    for s in sets:
        if s[0] > R_MAX or s[1] > G_MAX or s[2] > B_MAX:
            return False
    return True


def game_power(sets: list[(int, int, int)]) -> int:
    mr = mg = mb = 0
    for s in sets:
        mr = max(mr, s[0])
        mg = max(mg, s[1])
        mb = max(mb, s[2])
    return mr * mg * mb


def part1(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = map(lambda x: x.strip(), f.readlines())
        res = 0
        for line in lines:
            idx, sets = parse_game(line)
            if game_possible(sets):
                res += idx
        return res


def part2(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = map(lambda x: x.strip(), f.readlines())
        res = 0
        for line in lines:
            idx, sets = parse_game(line)
            res += game_power(sets)
        return res


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
