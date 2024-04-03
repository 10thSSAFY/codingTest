N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

dp = [0] * 1000001
for i in A_list:
    dp[i] += 1

result = 0
for i in B_list:
    if dp[i]:
        dp[i] -= 1
    else :
        result += 1

print(result)