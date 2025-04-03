N, A, B = map(int, input().split())
r = 0
while A != B:
    A -= A // 2
    B -= B // 2
    r += 1
    
print(r)