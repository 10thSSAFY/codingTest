input = __import__('sys').stdin.readline

A = input().rstrip()
B = input().rstrip()

cnt = [0] * 26
result = 0

for a in A:
    cnt[ord(a) - 97] += 1

for b in B:
    cnt[ord(b) - 97] -= 1

for n in cnt:
    result += abs(n)

print(result)
