N = int(input())
lst = list(map(int, input().split()))

y = 0
m = 0
for num in lst:
    y += (num // 30 + 1) * 10
    m += (num // 60 + 1) * 15

if y > m:
    print("M", m)
elif y == m:
    print("Y M", m)
else:
    print("Y", y)
