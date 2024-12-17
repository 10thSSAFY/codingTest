def find_num(num):
    global digit, result

    while True:
        if digit == 0:
            result += str(currSum[0][num])
            return

        for i in range(digit, 10):
            if currSum[digit][i] >= num:
                result += str(i)
                pos = num - max(currSum[digit][i - 1], currSum[digit - 1][9])
                num = currSum[digit - 1][digit - 1] + pos - 1
                digit -= 1
                break


def solution(num):
    global top_num, digit

    while top_num < num:
        digit += 1
        if digit == 10:
            return False

        for i in range(digit, 10):
            dp[digit][i] = sum(dp[digit - 1][:i])
            currSum[digit][i] = max(dp[digit][i] + currSum[digit][i-1], dp[digit][i] + currSum[digit - 1][9])
        top_num += sum(dp[digit])

    return True


N = int(input())

result = -1
top_num = 9
digit = 0
dp = [[0] * 10 for _ in range(10)]
currSum = [[0] * 10 for _ in range(10)]
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
currSum[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = ''
if solution(N):
    find_num(N)
    print(result)
else:
    print(-1)