def part1(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        res = 0
        for line in lines:
            _, card = line.split(":")
            l, r = card.split("|")
            li = set(map(lambda x: int(x), l.split()))
            ri = set(map(lambda x: int(x), r.split()))
            v = len(li & ri)
            if v > 0:
                res += 2 ** (v - 1)
        return res


def part2(input_txt: str) -> int:
    with open(input_txt) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        copies = [1] * len(lines)
        for idx, line in enumerate(lines):
            _, card = line.split(":")
            l, r = card.split("|")
            li = set(map(lambda x: int(x), l.split()))
            ri = set(map(lambda x: int(x), r.split()))
            v = len(li & ri)
            for j in range(idx + 1, idx + v + 1):
                copies[j] += copies[idx]
        return sum(copies)


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
