def up():
    global result
    cnt = -1
    for channel in range(N, 1000001):
        cnt += 1
        for b in broken:
            if str(b) in str(channel):
                break
        else:
            result = min(result, len(str(channel)) + cnt)
            return


def down():
    global result
    cnt = -1
    for channel in range(N, -1, -1):
        cnt += 1
        for b in broken:
            if str(b) in str(channel):
                break
        else:
            result = min(result, len(str(channel)) + cnt)
            return


N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []

result = abs(N - 100)
up()
down()
print(result)
