def solution(num1, num2):
    global result
    min_num = min(cnt[num1], cnt[num2])
    cnt[num1] -= min_num
    cnt[num2] -= min_num
    result += (num1 ^ num2) * min_num


N = int(input())
lst = list(map(int, input().split()))

cnt = [0, 0, 0, 0]
for l in lst:
    cnt[l] += 1

result = 0
solution(0, 3)
solution(1, 2)
solution(0, 2)
solution(1, 3)
solution(0, 1)
solution(2, 3)
print(result)