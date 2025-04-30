T = int(input())
for _ in range(T):
    A, B = input().split()
    cnt = [0] * 26
    for i in range(len(A)):
        cnt[ord(A[i]) - 97] += 1

    for j in range(len(B)):
        cnt[ord(B[j]) - 97] -= 1

    for i in range(26):
        if cnt[i] != 0:
            result = 'are NOT anagrams.'
            break
    else:
        result = 'are anagrams.'

    print(f'{A} & {B} {result}')
