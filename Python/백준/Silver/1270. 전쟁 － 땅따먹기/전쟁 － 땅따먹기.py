import sys
input = sys.stdin.readline

def main():
  T = int(input())
  for _ in range(T):
      d = dict()
      t, *lst = map(int, input().split())
      max_val = 0
      max_key = 0 
      for i in range(len(lst)):
          num = int(lst[i])
          if num not in d:
              d[num] = 1
          else:
              d[num] += 1
          if d[num] > max_val:
              max_val = d[num]
              max_key = num
      if max_val > t / 2:
          # 전쟁 끝
          print(max_key)
      else:
          print('SYJKGW')

main()