N = int(input())
P = int(input())

dc = 0
if N >= 20:
    dc = max(dc, P // 4)
if N >= 15:
    dc = max(dc, 2000)
if N >= 10:
    dc = max(dc, P // 10)
if N >= 5:
    dc = max(dc, 500)

print(max(0, P - dc))