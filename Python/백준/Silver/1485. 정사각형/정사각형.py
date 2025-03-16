input = __import__("sys").stdin.readline


def distance(p1,p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


T = int(input())
for _ in range(T):
    arr = []
    for _ in range(4):
        x,y = map(int, input().split())
        arr.append((x,y))

    arr.sort()    
    p = arr[0]
    arr[2], arr[3] = arr[3], arr[2]
    d = distance(p, arr[1])
    l = distance(p, arr[2])
    ans = 1
    for i in range(1, 4):
        if d != distance(arr[i], arr[(i + 1) % 4]):
            ans = 0
    if l != distance(arr[1], arr[3]):
        ans = 0
    print(ans)
