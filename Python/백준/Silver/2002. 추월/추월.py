input = __import__('sys').stdin.readline

N = int(input())

D_cars = dict()
Y_cars = dict()

for i in range(N):
    D_cars[input().rstrip()] = i

for i in range(N):
    Y_cars[input().rstrip()] = i

cnt = 0
Y_keys = list(Y_cars.keys())

for i in range(0, N - 1):
    for j in range(i + 1, N):
        if D_cars[Y_keys[j]] < D_cars[Y_keys[i]]:
            cnt += 1
            break

print(cnt)
