N = int(input())
player = []
result = []

for _ in range(N):
    a = input()
    player.append(a[0])

first_names = set(player)

for i in first_names:
    if player.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")