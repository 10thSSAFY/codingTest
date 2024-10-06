N = int(input())

nums = [0] * 10
curr = 0
num = N
while num:
    curr += num % 10
    nums[num % 10] += 1
    num //= 10

result = ''
if curr % 3 or not nums[0]:
    print(-1)
else:
    for i in range(9, -1, -1):
        result += str(i) * nums[i]

print(result)