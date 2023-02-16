from collections import defaultdict
N = int(input())

dict = defaultdict(int)

for i in range(N):
  num = int(input())
  dict[num] += 1

# print(dict)

ans = 0
for value in dict.values():
  ans += value*(value-1)//2

print(ans)