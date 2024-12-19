N = int(input())
lst = list(map(int, input().split()))

currSum = [[0] * N for _ in range(2)]
currSum[0][0] = lst[0]
currSum[1][0] = -int(1e9)
for i in range(1, N):
    currSum[0][i] = max(currSum[0][i - 1] + lst[i], lst[i])
    currSum[1][i] = max(currSum[0][i - 1], currSum[1][i - 1] + lst[i])

print(max(max(currSum[0]), max(currSum[1])))