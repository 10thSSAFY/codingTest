def solution():
    idx = 0
    res = 0
    latest_end = (3, 1)
    while idx < N:
        sm, sd, em, ed = arr[idx]
        if (sm, sd) <= latest_end < (em, ed):
            max_end = (em, ed)
            while idx < N - 1:
                nsm, nsd, nem, ned = arr[idx + 1]
                if latest_end < (nsm, nsd):
                    break
                if max_end < (nem, ned):
                    max_end = (nem, ned)
                idx += 1

            res += 1
            latest_end = max_end

            if (11, 30) < latest_end:
                return res
        idx += 1
    return 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
result = solution()
print(result)
