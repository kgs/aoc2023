def part1(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = map(lambda x: x.strip(), f.readlines())
        res = 0
        for line in lines:
            digits = list(filter(lambda x: x.isdigit(), line))
            res += int(digits[0]) * 10 + int(digits[-1])
        return res


def starts_with_special_digit(s: str) -> (bool, int):
    # digits + written ones
    t = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    if len(s) == 0:
        return False, None
    if s[0].isdigit():
        return True, int(s[0])
    for w in t.keys():
        if s.startswith(w):
            return True, t[w]
    return False, None


def part2(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = map(lambda v: v.strip(), f.readlines())
        res = 0
        for line in lines:
            x = 0
            for i in range(len(line)):
                ok, val = starts_with_special_digit(line[i:])
                if ok:
                    x = val * 10
                    break
            for i in range(len(line) - 1, -1, -1):
                ok, val = starts_with_special_digit(line[i:])
                if ok:
                    x += val
                    break
            res += x
        return res


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
