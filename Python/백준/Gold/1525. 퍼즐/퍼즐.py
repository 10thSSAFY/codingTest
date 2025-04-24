from collections import deque

D = {'0': [1, 3], '1': [0, 2, 4], '2': [1, 5],
     '3': [0, 4, 6], '4': [1, 3, 5, 7], '5': [2, 4, 8],
     '6': [3, 7], '7': [4, 6, 8], '8': [5, 7]}

board = ''
for _ in range(3):
    n1, n2, n3 = input().split()
    board += n1
    board += n2
    board += n3

S = set()
S.add(board)
queue = deque([(board, 0)])

result = -1
while queue:
    board, cnt = queue.popleft()
    if board == '123456780':
        result = cnt
        break

    zero_pos = board.index('0')
    for n in D[str(zero_pos)]:
        new_board = ''
        for i in range(9):
            if i == zero_pos:
                new_board += board[n]
            elif i == n:
                new_board += '0'
            else:
                new_board += board[i]

        if new_board in S:
            continue

        S.add(new_board)
        queue.append((new_board, cnt + 1))

print(result)
