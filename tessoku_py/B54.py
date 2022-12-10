from collections import defaultdict
N = int(input())

dict = defaultdict(int)
for i in range(N):
  inp = int(input())
  dict[inp] += 1

# print(dict)

ans = 0
for value in dict.values():
  # print(value)
  ans += value*(value-1)//2

print(ans)