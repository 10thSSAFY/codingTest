participant = 0
score = 0

for i in range(1, 6):
    s = sum(map(int, input().split()))
    if score < s:
        participant = i
        score = s

print(participant, score)