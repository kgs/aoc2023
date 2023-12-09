import functools
import itertools


def solve(input_txt):
    with open(input_txt) as f:
        lines = map(lambda v: v.strip(), f.readlines())
        res1 = res2 = 0
        for line in lines:
            r = [*map(int, line.split())]
            last, first = [], []
            while any(r):
                last.append(r[-1])
                first.append(r[0])
                r = [b - a for a, b in itertools.pairwise(r)]
            res1 += sum(last)
            res2 += functools.reduce(lambda x, y: y - x, reversed(first))
        return res1, res2


if __name__ == '__main__':
    print(*solve("part1.txt"))
