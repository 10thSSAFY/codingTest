N = int(input())
lst = list(map(int, input().split()))

count = [0] * 1000001
stack = []
res = [-1] * N
for num in lst:
    count[num] += 1

for i in range(N):
    while stack and count[lst[stack[-1]]] < count[lst[i]]:

        res[stack.pop()] = lst[i]
    stack.append(i)

print(" ".join(map(str,res)))