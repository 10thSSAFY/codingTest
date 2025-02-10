def solution(one, three, N):
    if N == 1:
        print(one, three)
        return

    solution(one, 6 - one - three, N - 1)
    print(one, three)
    solution(6 - one - three, three, N - 1)


N = int(input())

print(2 ** N - 1)
if N <= 20:
    solution(1, 3, N)
