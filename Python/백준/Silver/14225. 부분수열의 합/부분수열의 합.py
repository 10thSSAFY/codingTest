def solution(depth, curr):
    if depth == N:
        S.add(curr)
        return

    if curr != 0 and curr not in S:
        S.add(curr)

    solution(depth + 1, curr + lst[depth])
    solution(depth + 1, curr)


N = int(input())
lst = list(map(int, input().split()))

S = set()
solution(0, 0)

result = 0
while True:
    result += 1
    if result not in S:
        break

print(result)