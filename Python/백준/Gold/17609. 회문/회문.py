import sys
input = sys.stdin.readline


def solution(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            temp = str[:right] + str[right + 1:]
            if temp[:] == temp[::-1]:
                return 1

            temp = str[:left] + str[left + 1:]
            if temp[:] == temp[::-1]:
                return 1

            return 2
    return 0


T = int(input())
for _ in range(T):
    res = solution(input().strip())
    print(res)