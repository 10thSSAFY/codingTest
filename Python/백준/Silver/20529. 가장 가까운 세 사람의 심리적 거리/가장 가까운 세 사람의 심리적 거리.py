input = __import__('sys').stdin.readline


def solution(p1,  p2):
	cnt = 0
	for i in range(4):
		if p1[i] != p2[i]:
			cnt += 1 
	return cnt


def check(a, b, c):
	cnt = solution(a, b)
	cnt += solution(b, c)
	cnt += solution(c, a)
	
	return cnt


T = int(input())
for _ in range(T):
	N = int(input())
	lst = list(input().split())
	if N > 32:
		print(0)
	else:
		result = __import__('sys').maxsize
		for i in range(N - 2):
			for j in range(i + 1, N - 1):
				for k in range(j + 1, N):
					result = min(result, check(lst[i], lst[j], lst[k]))
					
		print(result)
