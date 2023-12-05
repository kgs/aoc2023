from typing import Any, Callable


def get_rules(input_txt: str, seeds_ranges: bool = False) -> (list[Any], list[list[(int, int, int)]]):
    with open(input_txt) as f:
        blocks = f.read().split("\n\n")
        seeds = list(map(int, blocks[0].split(":")[1].split()))
        if seeds_ranges:
            tmp = []
            for i in range(len(seeds) // 2):
                tmp.append((seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1]))
            seeds = tmp
        maps = [[list(map(int, r.split())) for r in b.splitlines()[1:]] for b in blocks[1:]]
        return seeds, maps


def calc(seed: int, maps: list[list[(int, int, int)]]) -> int:
    v = seed
    for m in maps:
        for rule in m:
            if rule[1] <= v < rule[1] + rule[2]:
                v = rule[0] + (v - rule[1])
                break
    return v


def part1(input_txt: str) -> int:
    seeds, maps = get_rules(input_txt)
    return min(calc(seed, maps) for seed in seeds)


def upper_bound(a: int, b: int, val: Callable[[int], int], target: int) -> int:
    left, right = a, b
    while left < right:
        mid = left + (right - left) // 2
        v = val(mid)
        if v <= target:
            left = mid + 1
        else:
            right = mid
    return left


def part2(input_txt: str) -> int:
    seeds_ranges, maps = get_rules(input_txt, seeds_ranges=True)
    lowest = 2 ** 42
    for lo, hi in seeds_ranges:
        # function calc(p) where p is from seed range [lo, hi) consists of some
        # ascending segments, we need to check first element of every segment as potential answer;
        # in every segment use binary search to find its end
        # XXX: you can construct counter-example for this algo, but (thankfully) it works here :)
        p = lo
        while p < hi:
            p_val = calc(p, maps)
            lowest = min(lowest, p_val)
            p = upper_bound(p, hi, lambda x: 0 if calc(x, maps) == p_val + (x - p) else 1, 0)
    return lowest


if __name__ == '__main__':
    p1_ans = part1("part1.txt")
    print(f"part1: {p1_ans}")
    p2_ans = part2("part1.txt")
    print(f"part2: {p2_ans}")
