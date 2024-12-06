from collections import deque

S = int(input())
dp = [[0] * 1001 for _ in range(1001)]
q = deque([(1, 0)])
result = 0
while q:
    x_screen, x_clip = q.popleft()
    if x_screen == S:
        result = dp[x_screen][x_clip]
        break

    for screen, clip in [(x_screen, x_screen), (x_screen + x_clip, x_clip), (x_screen - 1, x_clip)]:
        if 0 <= screen < 1001 and 0 <= clip < 1001 and not dp[screen][clip]:
            q.append((screen, clip))
            dp[screen][clip] = dp[x_screen][x_clip] + 1

print(result)