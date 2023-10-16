import sys
def input(): return sys.stdin.readline()[:-1]
N = int(input())
# import math
from collections import defaultdict
import heapq

S = []
C = []
dic = defaultdict(int)
Q = []
cnt = 0
for i in range(N):
  s, c = map(int, input().split())
  # S.append(s)
  # C.append(c)
  heapq.heappush(Q, s)
  dic[s] += c
  cnt += c

# print(dic)
# print(cnt)

# print(math.log2(16))
# print(int(math.log2(16)))

while len(Q) > 0:
  s = heapq.heappop(Q)
  c = dic[s]
  # numSyn = int(math.log2(c))
  numSyn = c//2
  if numSyn!=0 and dic[2*s]==0:
    heapq.heappush(Q, 2*s)
  dic[s] -= 2*numSyn
  dic[2*s] += numSyn
  cnt -= numSyn

print(cnt)