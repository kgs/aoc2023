def count_one_dim(g, key, expand):
    g = sorted(g, key=key)
    n = len(g)
    res = 0
    for i in range(1, n):
        d = key(g[i]) - key(g[i - 1])
        if d > 1:
            res += (i * (n - i)) * expand
    return res


def solve(input_txt):
    with open(input_txt) as f:
        m = list(map(lambda v: v.strip(), f.readlines()))
        g = []
        for y in range(len(m)):
            for x in range(len(m[0])):
                if m[y][x] == '#':
                    g.append((x, y))
        res = 0
        n = len(g)
        for i in range(n):
            for j in range(i + 1, n):
                res += abs(g[i][1] - g[i][1]) + abs(g[j][0] - g[j][0])
        for e in [1, 1000000 - 1]:
            yield res + count_one_dim(g, lambda v: v[0], e) + count_one_dim(g, lambda v: v[1], e)


if __name__ == '__main__':
    print(*solve("part1.txt"))
