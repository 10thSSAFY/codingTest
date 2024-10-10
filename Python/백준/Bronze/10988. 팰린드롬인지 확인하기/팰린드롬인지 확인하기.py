S = input()

if S[::1] == S[::-1]:
    print(1)
else:
    print(0)