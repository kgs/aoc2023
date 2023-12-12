from functools import cache


@cache
def count(row, current_group, groups_left):
    if len(row) == 0:
        if len(groups_left) == 0 and current_group == 0:
            return 1
        if len(groups_left) == 1 and 0 < current_group == groups_left[0]:
            return 1
        return 0

    match row[0]:
        case ".":
            if current_group > 0:
                if len(groups_left) > 0 and current_group == groups_left[0]:
                    return count(row[1::], 0, groups_left[1::])
                return 0
            else:
                return count(row[1::], 0, groups_left)
        case "#":
            return count(row[1::], current_group + 1, groups_left)
        case "?":
            return (count("." + row[1::], current_group, groups_left)
                    + count("#" + row[1::], current_group, groups_left))


def solve(input_txt):
    with open(input_txt) as f:
        lines = list(map(lambda v: v.strip(), f.readlines()))
        part1 = part2 = 0
        for i, line in enumerate(lines):
            row, groups = line.split()
            groups = list(map(int, groups.split(",")))
            part1 += count(row, 0, tuple(groups))
            row = "?".join([row] * 5)
            groups = groups * 5
            part2 += count(row, 0, tuple(groups))
        return part1, part2


if __name__ == '__main__':
    print(*solve("part1.txt"))
