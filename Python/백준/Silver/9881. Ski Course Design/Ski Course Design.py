import sys
input = sys.stdin.readline

N = int(input())
hills = [0] * 101
for _ in range(N):
    hills[int(input())] += 1

min_cost = sys.maxsize

for i in range(0, 84):
    cost = 0
    for j in range(i):
        if hills[j] > 0:
            cost += hills[j] * ((i - j) ** 2)
    for j in range(i + 17, 101):
        if hills[j] > 0:
            cost += hills[j] * ((j - (i + 17)) ** 2)
    min_cost = min(min_cost, cost)

print(min_cost)
