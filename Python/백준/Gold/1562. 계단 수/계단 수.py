def count_stair_numbers(n):
    # MOD 상수 정의
    MOD = 1000000000

    # dp[i][j][used]: i자리, 마지막 숫자가 j이고, used 상태의 계단 수 개수
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

    # 초기값 설정 - 한 자리 숫자의 경우
    for i in range(1, 10):  # 0으로 시작하는 수는 제외
        dp[1][i][1<<i] = 1  # 각 숫자의 사용 여부를 비트마스크로 표시

    # n자리 숫자에 대해 계산
    for length in range(1, n):
        for last in range(10):
            for used in range(1 << 10):
                if dp[length][last][used] == 0:
                    continue

                # 이전 숫자보다 1 큰 경우
                if last < 9:
                    next_used = used | (1 << (last + 1))
                    dp[length + 1][last + 1][next_used] = (dp[length + 1][last + 1][next_used] + dp[length][last][used]) % MOD

                # 이전 숫자보다 1 작은 경우
                if last > 0:
                    next_used = used | (1 << (last - 1))
                    dp[length + 1][last - 1][next_used] = (dp[length + 1][last - 1][next_used] + dp[length][last][used]) % MOD

    # 모든 숫자를 사용한 경우의 답 계산
    answer = 0
    all_used = (1 << 10) - 1  # 모든 숫자가 사용된 상태

    for last in range(10):
        answer = (answer + dp[n][last][all_used]) % MOD

    return answer

# 입력 처리
n = int(input())
print(count_stair_numbers(n))
