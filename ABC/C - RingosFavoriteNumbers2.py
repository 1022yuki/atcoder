# from itertools import combinations
# import scipy

from collections import defaultdict
from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

dict = defaultdict(int)

for x in A:
  dict[x%200] += 1

# print(dict)

cnt = 0
for x in dict.values():
  cnt += x*(x-1) // 2

print(cnt)