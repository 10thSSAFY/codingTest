import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def preorder(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return

    root = postOrder[post_r]
    print(root, end=' ')

    in_root = inOrder_idx[root]
    left = in_root - in_l
    right = in_r - in_root

    preorder(in_l, in_root - 1, post_l, post_l + left - 1)
    preorder(in_root + 1, in_r, post_r - right, post_r - 1)


N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

inOrder_idx = [0] * (N + 1)
for i in range(N):
    inOrder_idx[inOrder[i]] = i

preorder(0, N - 1, 0, N - 1)
