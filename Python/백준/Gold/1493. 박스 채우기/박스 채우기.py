def solution(l, w, h, blocks):
    blocks.sort(reverse=True, key=lambda x: x[0])
    total_count = 0
    volume = l * w * h
    used_volume = 0

    for i in range(len(blocks)):
        size = 2 ** blocks[i][0]
        count = blocks[i][1]

        if volume <= used_volume:
            break

        max_count = (l // size) * (w // size) * (h // size)
        max_count -= used_volume // (size ** 3)
        use_count = min(count, max_count)

        used_volume += use_count * (size ** 3)
        total_count += use_count

    if used_volume >= volume:
        return total_count
    else:
        return -1


L, W, H = map(int, input().split())
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = solution(L, W, H, arr)
print(result)