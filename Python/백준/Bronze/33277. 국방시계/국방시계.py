def solution(time):
    for HH in range(24):
        if HH / 24 <= time < (HH + 1) / 24:
            time -= HH/24
            for MM in range(60):
                if MM / (24 * 60) <= time < (MM + 1) / (24 * 60):
                    if 0 <= HH < 10 and 0 <= MM < 10:
                        return f'0{HH}:0{MM}'
                    elif 0 <= HH < 10:
                        return f'0{HH}:{MM}'
                    elif 0 <= MM < 10:
                        return f'{HH}:0{MM}'
                    else:
                        return f'{HH}:{MM}'


N, M = map(int, input().split())
t = M / N

if M == 0:
    print("00:00")
elif M == N:
    print("24:00")

else:
    result = solution(t)
    print(result)
