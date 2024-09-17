while True:
    num1, num2 = input().split()

    if num1 == '0' and num2 == '0':
        break

    N = max(len(num1), len(num2))
    num1 = (N - len(num1)) * '0' + num1
    num2 = (N - len(num2)) * '0' + num2

    carry = 0
    cnt = 0
    for i in range(N - 1, -1, -1):
        if (int(num1[i]) + int(num2[i]) + carry) >= 10:
            carry = 1
            cnt += 1
        else:
            carry = 0

    print(cnt)