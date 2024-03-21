import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    num = int(input())
    if not stack:
        stack.append(num)
        continue
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)

print(len(stack))
