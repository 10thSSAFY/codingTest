lst = [0] * 1001
curr_sum = 0
for _ in range(10):
    n = int(input())
    lst[n] += 1
    curr_sum += n

print(curr_sum // 10)
print(lst.index(max(lst)))