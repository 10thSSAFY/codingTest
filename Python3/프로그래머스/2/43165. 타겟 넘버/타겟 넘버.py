def solution(numbers, target):
    N = len(numbers)
    arr = [[] for _ in range(N + 1)]
    arr[0].append(0)
    for i in range(N):
        for a in arr[i]:
            arr[i + 1].append(a + numbers[i])
            arr[i + 1].append(a - numbers[i])
    answer = arr[N].count(target)
    return answer