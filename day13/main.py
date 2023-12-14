def is_reflection(p, v):
    n = len(p)
    i = 0
    while 0 <= v - i and v + 1 + i < n:
        if p[v - i] != p[v + 1 + i]:
            return False
        i += 1
    return True


def find_reflection_horizontally(p, skip_reflection):
    for v in range(len(p) - 1):
        # check v, v+1 reflection
        if v + 1 != skip_reflection and is_reflection(p, v):
            return v + 1
    return 0


def rotate_matrix_right(m):
    rows, cols = len(m), len(m[0])
    tmp = [[' ' for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            tmp[j][rows - 1 - i] = m[i][j]

    return [''.join(r) for r in tmp]


def find_reflection(p, reflection_to_skip=(0, 0)):
    skip_a, skip_b = reflection_to_skip
    a1 = find_reflection_horizontally(p, skip_a)
    p = rotate_matrix_right(p)
    b1 = find_reflection_horizontally(p, skip_b)
    return a1, b1


def flip(p, x, y):
    c = p[y][x]
    nc = "." if c == "#" else "#"
    p[y] = p[y][:x] + nc + p[y][x + 1:]
    return p


def find_smudge_reflection(p, orig_reflection):
    for y in range(len(p)):
        for x in range(len(p[0])):
            p = flip(p, x, y)
            a, b = find_reflection(p, orig_reflection)
            p = flip(p, x, y)
            if a + b > 0:
                return a, b


def solve(input_txt):
    with open(input_txt) as f:
        patterns = f.read().strip().split("\n\n")
        part1 = part2 = 0
        for p in patterns:
            p = p.splitlines()
            a1, b1 = find_reflection(p)
            a2, b2 = find_smudge_reflection(p, (a1, b1))
            part1 += a1 * 100 + b1
            part2 += a2 * 100 + b2
        return part1, part2


if __name__ == '__main__':
    print(*solve("part1.txt"))
