N = int(input())
distance = list(map(int, input().split()))
station = list(map(int, input().split()))
cur_distance = [0] * N

for i in range(N-2, -1, -1):
    cur_distance[i] = distance[i] + cur_distance[i+1]

res = float('inf')
tmp = 0
for j in range(N-1):
    res = min(tmp + station[j] * cur_distance[j], res)
    tmp += station[j] * distance[j]

print(res)