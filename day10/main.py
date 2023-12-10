import sys

DIRS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

PIPES = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE",
    ".": ""
}


def find_s(m) -> (int, int):
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "S":
                return x, y


def dfs(m, v: (int, int), prev: (int, int), loop: set) -> int:
    vx, vy = v
    p = m[vy][vx]
    loop.add(v)
    if p == "S":
        return 1
    p_dirs = PIPES[p]
    for d in p_dirs:
        dx, dy = DIRS[d]
        nx, ny = vx + dx, vy + dy
        if (nx, ny) != prev:
            return 1 + dfs(m, (nx, ny), v, loop)


def scan(m, loop: set) -> int:
    res = 0
    for y in range(len(m)):
        inside = False
        start_tile = None
        for x in range(len(m[0])):
            t = m[y][x]
            match (x, y) in loop, t:
                case False, _:
                    res += 1 if inside else 0
                case True, "|":
                    inside = not inside
                case True, "L" | "F":
                    start_tile = t
                case True, "J":
                    if start_tile == "F":
                        inside = not inside
                case True, "7":
                    if start_tile == "L":
                        inside = not inside
    return res


def solve(input_txt):
    with open(input_txt) as f:
        m = list(map(lambda v: v.strip(), f.readlines()))
        m = ["." + row + "." for row in m]
        m = ["." * len(m[0])] + m + ["." * len(m[0])]
        sx, sy = find_s(m)
        loop = set()  # part2
        for d in DIRS.keys():
            dx, dy = DIRS[d]
            nx, ny = sx + dx, sy + dy
            if d in PIPES[m[ny][nx]]:
                part1 = dfs(m, (nx, ny), (sx, sy), loop) // 2
                break
        m[sy] = m[sy][:sx] + "7" + m[sy][sx + 1:]  # TODO: S replaced manually, write algo for that
        part2 = scan(m, loop)
        return part1, part2


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(*solve("part1.txt"))
