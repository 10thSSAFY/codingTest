def solution(currSum, start, depth):
    global result

    if depth == N:
        if currSum not in S:
            S.add(currSum)
            result += 1
        return

    for i in range(start, 4):
        solution(currSum + num[i], i, depth + 1)


N = int(input())

num = [1, 5, 10, 50]
S = set()
result = 0
solution(0, 0, 0)
print(result)