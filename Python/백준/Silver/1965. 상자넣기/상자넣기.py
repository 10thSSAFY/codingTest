def max_nested_boxes(n, boxes):
    # 각 위치에서 가능한 최대 상자 개수를 저장
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if boxes[j] < boxes[i]:  # 현재 상자에 이전 상자를 넣을 수 있는지 확인
                dp[i] = max(dp[i], dp[j] + 1)  # 최대 상자 개수 갱신

    return max(dp)  # 가능한 최대 상자 개수 반환

# 입력 처리
n = int(input())
boxes = list(map(int, input().split()))
print(max_nested_boxes(n, boxes))