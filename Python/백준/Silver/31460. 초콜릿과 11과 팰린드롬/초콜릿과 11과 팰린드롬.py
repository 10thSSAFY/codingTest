import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(11)
    else:
        print('1'+ '2'*(N-2) +'1')