import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict

N = int(input())
A = [0, 0]+list(map(int, input().split()))

# print(A)

buka_dir = defaultdict(list)

for i in range(2, N+1):
  buka_dir[A[i]].append(i)

# print(buka_dir)

buka_num = [-1]*(N+1)

def rec(i):
  if buka_num[i] != -1:
    return buka_num[i]
  if buka_dir[i] == []:
    buka_num[i] = 0
    return 0
  sum = 0
  for ni in buka_dir[i]:
    sum += rec(ni)+1
  buka_num[i] = sum
  return sum

rec(1)
print(*buka_num[1:])