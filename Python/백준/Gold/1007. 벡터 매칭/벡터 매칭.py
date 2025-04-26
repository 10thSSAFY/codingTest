input = __import__('sys').stdin.readline
import math
import itertools


T = int(input())
results = []

for _ in range(T):
    N = int(input())
    points = []

    sum_x, sum_y = 0, 0
    for _ in range(N):
        x, y = map(int, input().split())
        sum_x += x
        sum_y += y
        points.append([x, y])

    res = math.inf
    combinations = list(itertools.combinations(points, int(N / 2)))
    combinations_len_half = int(len(combinations) / 2)
    for sum_coord in combinations[:combinations_len_half]:
        sum_coord = list(sum_coord)

        x1_total = 0
        y1_total = 0
        for x1, y1 in sum_coord:
            x1_total += x1
            y1_total += y1

        x2_total = sum_x - x1_total
        y2_total = sum_y - y1_total

        res = min(res, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))

    results.append(res)

for result in results:
    print(str(result))