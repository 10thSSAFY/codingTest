def solution(cnt, word):
    global result

    if cnt == N:
        if word not in result:
            result.add(word)
        return

    for i in range(N):
        if not bit[i]:
            a = word[-1] if len(word) > 0 else False
            b = S[i]
            if len(word) > 0 and word[-1] == S[i]:
                continue
            bit[i] = True
            solution(cnt + 1, word + S[i])
            bit[i] = False


S = input()
N = len(S)
bit = [False] * (N)
result = set()
solution(0, '')

print(len(result))