input = __import__('sys').stdin.readline

N = int(input())
lst = []
for _ in range(N):
    name, d, m, y = input().split()
    lst.append((name, int(d), int(m), int(y),))
    lst.sort(key=lambda x: (x[3], x[2], x[1]))

print(lst[-1][0])
print(lst[0][0])