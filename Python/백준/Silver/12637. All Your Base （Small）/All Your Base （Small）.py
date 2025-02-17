def solution(depth, num):
    global result

    if num > result:
        return

    if depth == len(lst):
        result = min(result, num)
        return

    for i in range(len(lst)):
        if depth == 0 and i == 0 and lst[i] == first_num:
            continue

        if not bit[i]:
            bit[i] = True
            solution(depth + 1, num + counts[i] * depth)
            bit[i] = False


T = int(input())
for tc in range(1, T + 1):
    symbol = input()
    S = set()
    lst = []
    for i in range(len(symbol)):
        if symbol[i] not in S:
            S.add(symbol[i])
            lst.append(symbol[i])

    if len(S) == 1:
        result = 2 ** len(symbol) - 1
        print(f'Case #{tc}: {result}')
    else:
        counts = [0] * len(lst)
        for j in range(len(lst)):
            num = lst[j]
            for k in range(len(symbol)):
                if symbol[len(symbol) - 1 - k] == num:
                    counts[j] += len(S) ** k

        first_num = symbol[0]

        bit = [False] * len(S)
        result = 10 ** 18
        solution(0, 0)
        print(f'Case #{tc}: {result}')
