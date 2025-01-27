def solution(depth):
    if depth == M:
        tmp = ' '.join(map(str, nums))
        if tmp not in S:
            S.add(tmp)
            print(tmp)
        return

    for i in range(N):
        if not bit[i]:
            bit[i] = True
            nums.append(lst[i])
            solution(depth + 1)
            nums.pop()
            bit[i] = False


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

bit = [False] * N
nums = []
S = set()
solution(0)
