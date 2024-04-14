import sys
input = sys.stdin.readline

def main():
    N = int(input())
    stack = []
    res = 0
    for _ in range(N):
        num = int(input())
        if not stack:
            stack.append(num)
        elif stack[-1] > num:
            res += len(stack)
            stack.append(num)
        elif stack[-1] <= num:
            while stack and stack[-1] <= num:
                stack.pop()
            res += len(stack)
            stack.append(num)

    return res

print(main())