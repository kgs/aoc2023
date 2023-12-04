from functools import reduce
from typing import Iterable


def get_points(input_txt: str) -> Iterable[int]:
    with open(input_txt) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        for line in lines:
            _, card = line.split(":")
            yield len(reduce(lambda a, b: a & b,
                             [set(map(lambda x: int(x), s.split())) for s in card.split("|")]))


def part1(input_txt: str) -> int:
    points = get_points(input_txt)
    return sum([2 ** (p - 1) for p in points if p > 0])


def part2(input_txt: str) -> int:
    points = list(get_points(input_txt))
    n = len(points)
    copies = [1] * n
    for i in range(n):
        for j in range(i + 1, i + points[i] + 1):
            copies[j] += copies[i]
    return sum(copies)


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
