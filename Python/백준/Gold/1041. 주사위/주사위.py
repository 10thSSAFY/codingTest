n = int(input())
nums = list(map(int, input().split()))

lst = []
result = 0
if n == 1:
    nums = sorted(nums)
    result += sum(nums[0:5])
else:
    lst.append(min(nums[0], nums[5]))
    lst.append(min(nums[1], nums[4]))
    lst.append(min(nums[2], nums[3]))
    lst = sorted(lst)

    d1 = lst[0]
    d2 = lst[0] + lst[1]
    d3 = lst[0] + lst[1] + lst[2]

    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    result += n1 * d1
    result += n2 * d2
    result += n3 * d3

print(result)