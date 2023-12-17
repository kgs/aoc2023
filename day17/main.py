import heapq
from dataclasses import dataclass

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


@dataclass(frozen=True, order=True)
class Node:
    straight_so_far: int
    from_dir: int
    pos: tuple[int, int]


def gen_neighbours(v: Node, blocks: list[list[int]],
                   max_x: int, max_y: int,
                   min_straight: int, max_straight: int) -> (Node, int):
    sdx, sdy = DIRS[v.from_dir]
    for dir_idx in range(4):
        dx, dy = DIRS[dir_idx]
        if sdx == -dx and sdy == -dy:
            # cannot go backward
            continue
        nx = v.pos[0] + dx
        ny = v.pos[1] + dy
        if not (0 <= nx < max_x and 0 <= ny < max_y):
            continue
        if dir_idx == v.from_dir:
            # going straight
            if v.straight_so_far == max_straight:
                continue
            yield Node(v.straight_so_far + 1, dir_idx, (nx, ny)), blocks[ny][nx]
        else:
            # turn
            if v.straight_so_far >= min_straight:
                yield Node(1, dir_idx, (nx, ny)), blocks[ny][nx]


def solve(input_txt, min_straight, max_straight):
    with open(input_txt) as f:
        blocks = [[int(c) for c in line.strip()] for line in f.readlines()]

        max_x, max_y = len(blocks[0]), len(blocks)
        start_block = (0, 0)
        end_block = (max_x - 1, max_y - 1)

        heap = [
            (0, Node(1, 0, start_block)),
            (0, Node(1, 2, start_block))
        ]  # (cost from start, node)
        visited = set()
        # simplified Dijkstra (never remove or update heap values)
        while heap:
            (cost, v) = heapq.heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            if v.pos == end_block and v.straight_so_far >= min_straight:
                return cost
            for w, c in gen_neighbours(v, blocks, max_x, max_y, min_straight, max_straight):
                if w in visited:
                    continue
                next_item = cost + c
                heapq.heappush(heap, (next_item, w))


if __name__ == '__main__':
    print(solve("part1.txt", 1, 3))
    print(solve("part1.txt", 4, 10))
