input = __import__('sys').stdin.readline

result = []
while True:
    S = list(input().rstrip())
    if '-' in S:
        break

    stack = []
    cnt = 0

    for i in range(len(S)):
        if S[i] == '{':
            stack.append('{')
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append('}')

    if not stack:
        cnt = 0
    else:
        for i in range(0, len(stack) - 1, 2):
            if stack[i] == stack[i + 1]:
                cnt += 1
            else:
                cnt += 2

    result.append(cnt)

for i in range(len(result)):
    print(f'{i + 1}. {result[i]}')