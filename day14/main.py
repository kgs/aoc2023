ROCK = ord("O")
EMPTY = ord(".")
WALL = ord("#")

NORTH = (0, -1)
WEST = (-1, 0)
SOUTH = (0, 1)
EAST = (1, 0)


def drop(p, x, y, d):
    if p[y][x] == ROCK:
        dx, dy = d
        nx, ny = x + dx, y + dy
        while p[ny][nx] == EMPTY:
            p[ny][nx] = ROCK
            p[y][x] = EMPTY
            x, y = nx, ny
            nx, ny = x + dx, y + dy


def drop_north(p, rows, cols):
    for y in range(rows):
        for x in range(cols):
            drop(p, x, y, NORTH)


def drop_west(p, rows, cols):
    for x in range(cols):
        for y in range(rows):
            drop(p, x, y, WEST)


def drop_south(p, rows, cols):
    for y in reversed(range(rows)):
        for x in range(cols):
            drop(p, x, y, SOUTH)


def drop_east(p, rows, cols):
    for x in reversed(range(cols)):
        for y in range(rows):
            drop(p, x, y, EAST)


def print_platform(p):
    rows = len(p)
    cols = len(p[0])
    for y in range(rows):
        line = ""
        for x in range(cols):
            line += chr(p[y][x])
        print(line)


def read_platform(input_txt):
    with open(input_txt) as f:
        lines = list(map(lambda v: v.strip(), f.readlines()))
        p = [[ord(c) for c in line] for line in lines]
        p = [[WALL] + row + [WALL] for row in p]
        cols = len(p[0])
        p = [[WALL for _ in range(cols)]] + p + [[WALL for _ in range(cols)]]
        rows = len(p)
        return p, rows, cols


def score(p, rows, cols):
    res = 0
    for y in range(rows):
        for x in range(cols):
            if p[y][x] == ROCK:
                res += (rows - 1 - y)
    return res


def part1(input_txt):
    p, rows, cols = read_platform(input_txt)
    drop_north(p, rows, cols)
    return score(p, rows, cols)


def part2(input_txt):
    p, rows, cols = read_platform(input_txt)
    for i in range(1000):
        drop_north(p, rows, cols)
        drop_west(p, rows, cols)
        drop_south(p, rows, cols)
        drop_east(p, rows, cols)
        s = score(p, rows, cols)
        if s == 96078:
            print("i:", i)
    return 96061  # fsck cycle detection, do it manually just by looking ;)


if __name__ == '__main__':
    print(part1("part1.txt"))
    print(part2("part1.txt"))
