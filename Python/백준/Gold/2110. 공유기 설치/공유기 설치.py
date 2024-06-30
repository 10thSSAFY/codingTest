import sys
input = sys.stdin.readline

def solution(s, e, lst):
    global result
    while (s <= e):
        m = (s + e) // 2
        now = lst[0]
        cnt = 1

        for num in lst:
            if num >= now + m:
                cnt += 1
                now = num

        if cnt >= C:
            s = m + 1
            result = m
        else:
            e = m - 1


N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

s, e = 1, lst[-1] - lst[0]
result = 0

solution(s, e, lst)
print(result)
