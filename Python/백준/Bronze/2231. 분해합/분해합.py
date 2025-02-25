# 자릿수의 합을 계산하는 함수
def digit_sum(number):
    total = 0
    while number > 0: # 마지막 자리까지 반복
        total += number % 10
        number //= 10 # 1의 자리 버림
    return total


N = int(input())

result = 0
for i in range(max(1, N - len(str(N)) * 9), N):  # 범위 설정 (불필요한 연산을 방지하기 위해 분해합의 가능성이 있는 범위 산정)
    decomposition_sum = i + digit_sum(i)
    if decomposition_sum == N:
        result = i
        break

print(result)
