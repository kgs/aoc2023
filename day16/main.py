import sys


def gen_dirs(c, v):
    vx, vy = v
    match c:
        case ".":
            yield v
        case "|":
            match v:
                case (0, _):
                    yield v
                case (1, 0) | (-1, 0):
                    yield 0, -vx
                    yield 0, vx
        case "-":
            match v:
                case (_, 0):
                    yield v
                case (0, 1) | (0, -1):
                    yield -vy, 0
                    yield vy, 0
        case "\\":
            yield vy, vx
        case "/":
            yield -vy, -vx


def visit(m, s, v, visited):
    if (s, v) in visited:
        return
    sx, sy = s
    if 0 <= sx < len(m[0]) and 0 <= sy < len(m):
        visited.add((s, v))
        for d in gen_dirs(m[sy][sx], v):
            dx, dy = d
            visit(m, (sx + dx, sy + dy), d, visited)


def send_beam(m, s, v):
    visited = set()
    visit(m, s, v, visited)
    return len(set([s for s, _ in visited]))


def part1(input_txt):
    with open(input_txt) as f:
        m = list(map(lambda l: l.strip(), f.readlines()))
        return send_beam(m, (0, 0), (1, 0))


def part2(input_txt):
    with open(input_txt) as f:
        m = list(map(lambda l: l.strip(), f.readlines()))
        max_x, max_y = len(m[0]), len(m)
        return max(
            max([send_beam(m, (x, 0), (0, 1)) for x in range(max_x)]),
            max([send_beam(m, (x, max_y - 1), (0, -1)) for x in range(max_x)]),
            max([send_beam(m, (0, y), (1, 0)) for y in range(max_y)]),
            max([send_beam(m, (max_x - 1, y), (-1, 0)) for y in range(max_y)]),
        )


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(part1("part1.txt"))
    print(part2("part1.txt"))
