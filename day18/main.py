import sys

DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

DIRS_IDX = ["R", "D", "L", "U"]


def flood(board, x, y):
    if board[y][x]:
        return 0
    board[y][x] = 1
    res = 1
    for d in DIRS.values():
        dx, dy = d
        res += flood(board, x + dx, y + dy)
    return res


def part1(input_txt):
    with (open(input_txt) as f):
        lines = list(map(lambda l: l.strip(), f.readlines()))
        n = 1000
        board = [[0] * n for _ in range(n)]
        sx, sy = n // 2, n // 2

        cx, cy = sx, sy
        res = 0
        for line in lines:
            d, steps, _ = line.split()
            dx, dy = DIRS[d]
            for i in range(int(steps)):
                nx = cx + dx * (i + 1)
                ny = cy + dy * (i + 1)
                board[ny][nx] = 1
                res += 1
            cx, cy = nx, ny

        res += flood(board, sx + 1, sy + 1)
        return res


def polygon_area(p):
    n = len(p)
    res = 0
    prev = n - 1
    for i in range(n):
        res += (p[prev][0] + p[i][0]) * (p[prev][1] - p[i][1])
        prev = i
    return abs(res // 2)


def part2(input_txt):
    with (open(input_txt) as f):
        lines = list(map(lambda l: l.strip(), f.readlines()))

        cx, cy = 0, 0
        p = []
        boundary_points = 0
        for line in lines:
            _, _, color = line.split()
            color = color.strip("(#)")
            d = DIRS_IDX[int(color[-1])]
            steps = int(color[:5], 16)
            boundary_points += steps
            dx, dy = DIRS[d]
            cx += dx * steps
            cy += dy * steps
            p.append((cx, cy))
        area = polygon_area(p)
        # Pick's theorem + shoelace formula
        return boundary_points // 2 + area + 1


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(part1("part1.txt"))
    print(part2("part1.txt"))
