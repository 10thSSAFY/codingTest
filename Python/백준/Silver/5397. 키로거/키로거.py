input = __import__('sys').stdin.readline

T = int(input())
for _ in range(T):
    k = input().rstrip()
    left = []
    right = []
    for w in k:
        if w == '<':
            if left:
                right.append(left.pop())
        elif w == '>':
            if right:
                left.append(right.pop())
        elif w == '-':
            if left:
                left.pop()
        else:
            left.append(w)
    left.extend(reversed(right))
    print(''.join(left))
