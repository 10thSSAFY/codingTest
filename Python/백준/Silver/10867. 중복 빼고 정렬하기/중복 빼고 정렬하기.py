input = __import__('sys').stdin.readline

N = int(input())
lst = sorted(list(set(map(int, input().split()))))
print(*lst)