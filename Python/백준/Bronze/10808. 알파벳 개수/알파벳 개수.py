w = input()
cnt = [0] * 26

for i in w:
    cnt[ord(i) - 97] += 1

print(*cnt)