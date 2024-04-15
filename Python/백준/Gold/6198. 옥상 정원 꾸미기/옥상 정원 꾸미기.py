import sys
input = sys.stdin.readline

def main():
    N = int(input())
    stack = []
    res = 0
    for _ in range(N):
        num = int(input())
        while stack and stack[-1] <= num:
            stack.pop()
        res += len(stack)
        stack.append(num)

    return res

print(main())