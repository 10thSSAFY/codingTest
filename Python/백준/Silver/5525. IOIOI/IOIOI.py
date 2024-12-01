N = int(input())
M = int(input())
S = input()

P = 'I'
for _ in range(N):
    P += 'OI'

result = 0
for i in range(M - N * 2):
    if S[i:i+(N * 2 + 1)] == P:
        result += 1

print(result)