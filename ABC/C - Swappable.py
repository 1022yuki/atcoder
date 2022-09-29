

from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

def nC2(n):
  return n*(n-1)//2

dict = defaultdict(int)

for x in A:
  dict[x] += 1

sum = 0
for value in dict.values():
  sum += nC2(value)

ans = nC2(N) - sum

print(ans)