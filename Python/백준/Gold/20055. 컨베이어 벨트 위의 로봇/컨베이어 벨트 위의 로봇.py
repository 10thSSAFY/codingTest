from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))

result = 0
robot = deque([False] * N)
zero = 0
while True:
    result += 1

    A.rotate(1)
    robot.rotate(1)
    robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and A[i + 1]:
            robot[i], robot[i + 1] = False, True
            A[i + 1] -= 1
            if not A[i + 1]:
                zero += 1
    robot[N - 1] = False

    if A[0]:
        robot[0] = True
        A[0] -= 1
        if not A[0]:
            zero += 1

    if zero >= K:
        break

print(result)
