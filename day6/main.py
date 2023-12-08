import functools


def solve(input_txt):
    with open(input_txt) as f:
        times = list(map(int, f.readline().split(":")[1].split()))
        records = list(map(int, f.readline().split(":")[1].split()))
        ret = [0] * len(times)
        for t in range(len(times)):
            for i in range(times[t]):
                c = (times[t] - i) * i
                if c > records[t]:
                    ret[t] += 1
        return functools.reduce((lambda x, y: x * y), ret)


if __name__ == '__main__':
    print(solve("part1.txt"))
    print(solve("part2.txt"))  # numbers glued together manually
