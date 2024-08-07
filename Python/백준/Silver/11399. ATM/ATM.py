N = int(input())
lst = list(map(int, input().split()))
lst.sort()

sum_lst = [0] * (N + 1)
for i in range(N):
    sum_lst[i + 1] = sum_lst[i] + lst[i]

print(sum(sum_lst))