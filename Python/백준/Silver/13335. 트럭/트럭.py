from collections import deque

n, w, L = map(int, input().split())
q = deque(list(map(int, input().split())))

bridge = deque([0] * w)
bw = 0
cnt = 0
while q:
    out_w = bridge.popleft()
    bridge.append(0)
    cnt += 1
    bw -= out_w
    if bw + q[0] <= L:
        in_w = q.popleft()
        bridge[w-1] = in_w
        bw += in_w

print(cnt + w)