N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())

Tn = 0
for shirt in shirts:
    Tn += shirt // T
    if shirt % T:
        Tn += 1

print(Tn)
print(N // P, N % P)
