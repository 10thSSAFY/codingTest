S = input()
stack = []

ans = 0
num = 1
for i in range(len(S)):
    if S[i] == '(':
        stack.append(S[i])
        num *= 2
    elif S[i] == '[':
        stack.append(S[i])
        num *= 3
    elif S[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if S[i-1] == '(':
            ans += num
        stack.pop()
        num //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if S[i-1] == '[':
            ans += num
        stack.pop()
        num //= 3

if stack:
    print(0)
else:
    print(ans)
