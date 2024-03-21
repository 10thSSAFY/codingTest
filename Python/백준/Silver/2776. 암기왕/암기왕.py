T = int(input())
for tc in range(1,T+1):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    note1 = set(note1)

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)