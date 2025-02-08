L = int(input())
M = 1234567891
r = 31
S = input()

answer = 0

for i in range(len(S)):
    num = ord(S[i]) - 96
    answer += num * (r ** i)

print(answer % M)
