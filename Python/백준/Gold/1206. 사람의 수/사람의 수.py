def solution(curr):
    for avg in lst:
        l, r = 0, 10 * curr
        while l <= r:
            m = (l + r) // 2
            new_avg = (m * 1000) // curr
            if new_avg == avg:
                if new_avg <= 10000:
                    break
                else:
                    return False
            elif new_avg > avg:
                r = m - 1
            else:
                l = m + 1
        else:
            return False
    return True


N = int(input())
lst = []
for _ in range(N):
    s1, s2 = input().split('.')
    lst.append(int(s1) * 1000 + int(s2))

for curr in range(1, 1001):
    if solution(curr):
        print(curr)
        break
