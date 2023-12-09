import functools


def diff(a):
    return [a[i] - a[i - 1] for i in range(1, len(a))]


def solve(input_txt):
    with open(input_txt) as f:
        lines = map(lambda v: v.strip(), f.readlines())
        res1 = res2 = 0
        for line in lines:
            r = list(map(int, line.split()))
            last = []
            first = []
            while not all([v == 0 for v in r]):
                last.append(r[-1])
                first.append(r[0])
                r = diff(r)
            res1 += sum(last)
            res2 += functools.reduce(lambda x, y: y - x, reversed(first))
        return res1, res2


if __name__ == '__main__':
    print(*solve("part1.txt"))
