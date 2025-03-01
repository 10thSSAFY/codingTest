str1 = [0] + list(input())
str2 = [0] + list(input())

len_1 = len(str1)
len_2 = len(str2)

arr = [[''] * len_1 for _ in range(len_2)]
for i in range(1, len_2):
    for j in range(1, len_1):
        if str1[j] == str2[i]:
            arr[i][j] = arr[i - 1][j - 1] + str1[j]
        else:
            if len(arr[i][j - 1]) > len(arr[i - 1][j]):
                arr[i][j] = arr[i][j - 1]
            else:
                arr[i][j] = arr[i - 1][j]

result = len(arr[-1][-1])
print(result)
if result != 0:
    print(arr[-1][-1])
