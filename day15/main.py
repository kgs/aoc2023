def calc_hash(s):
    res = 0
    for c in s:
        res = (res + ord(c)) * 17
        res %= 256
    return res


def part1(input_txt):
    with open(input_txt) as f:
        elements = f.read().strip().split(",")
        return sum([calc_hash(e) for e in elements])


def part2(input_txt):
    with open(input_txt) as f:
        steps = f.read().strip().split(",")
        boxes = [dict() for _ in range(256)]
        slot_id = 0
        for s in steps:
            match s.split("="):
                case label, focal:
                    focal = int(focal)
                    b = calc_hash(label)
                    lens = [slot_id, focal]
                    if label in boxes[b]:
                        boxes[b][label][1] = focal
                    else:
                        boxes[b][label] = lens
                case [label] if label.endswith("-"):
                    label = label[:-1]
                    b = calc_hash(label)
                    if label in boxes[b]:
                        del boxes[b][label]
            slot_id += 1
        res = 0
        for i in range(len(boxes)):
            ordered_focals = list(map(lambda lns: lns[1], sorted(boxes[i].values(), key=lambda v: v[0])))
            for j, focal in enumerate(ordered_focals):
                res += (i + 1) * (j + 1) * focal
        return res


if __name__ == '__main__':
    print(part1("part1.txt"))
    print(part2("part1.txt"))
