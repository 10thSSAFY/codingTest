input = __import__('sys').stdin.readline


def max_score_of_stairs(stairs):
    n = len(stairs)

    if n == 0:
        return 0
    elif n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]

    # 각 계단을 오르는 최대값을 저장할 변수
    dp = [0] * n
    # 첫번째 계단까지의 최대값
    dp[0] = stairs[0]
    # 두번째 계단까지의 최대값
    dp[1] = stairs[0] + stairs[1]
    # 세번째 계단까지의 최대값
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    # 네번째부터 마지막까지 반복하며, 각 계단의 최대값 구하기
    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

    return dp[-1]


# 계단 점수를 입력받습니다.
stairs = [int(input()) for _ in range(int(input()))]
print(max_score_of_stairs(stairs))
