import math


def read_input(input_txt):
    with open(input_txt) as f:
        ins, m_str = f.read().split("\n\n")
        ins = ins.strip()
        m = {}
        for line in m_str.split("\n"):
            x, lr = line.split("=")
            l, r = map(lambda c: c.strip(" ()"), lr.split(","))
            m[x.strip()] = (l, r)
        return ins, m


def part1(input_txt):
    ins, m = read_input(input_txt)
    res = ic = 0
    curr = "AAA"
    while curr != "ZZZ":
        curr = m[curr][0 if ins[ic] == "L" else 1]
        ic = (ic + 1) % len(ins)
        res += 1
    return res


def part2(input_txt):
    ins, m = read_input(input_txt)
    curr = [c for c in m.keys() if c.endswith("A")]
    res = []
    for c in curr:
        tmp = ic = 0
        while not c.endswith("Z"):
            c = m[c][0 if ins[ic] == "L" else 1]
            ic = (ic + 1) % len(ins)
            tmp += 1
        res.append(tmp)
    return math.lcm(*res)


if __name__ == '__main__':
    print(part1("part1.txt"))
    print(part2("part1.txt"))
