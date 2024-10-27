S = input().strip()
B = input().strip()

stack = []
B_len = len(B)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-B_len:]) == B:
        for _ in range(B_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')