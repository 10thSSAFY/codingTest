N = int(input())

div = 1000000007
dp = [0] * 1516
dp[1] = (0, 0, 1)
for i in range(2, N + 1):
    (zro, one, two) = dp[i - 1]
    dp[i] = ((one + two) % div, (zro + two) % div, (zro + one) % div)

print(dp[N][0])