# from collections import defaultdict
# import sys
# sys.setrecursionlimit(1000000)
from functools import lru_cache

N = int(input())

# cost = [0]*(N+1)
# done = [False]*(N+1)

# cost = defaultdict(int)
# done = defaultdict(int)

# def rec(i):
#   # if done[i] == 1:
#   #   return cost[i]
#   if i == 0:
#     cost[i] = 1
#   else:
#     cost[i] = rec(i//2)+rec(i//3)
#   # done[i] = 1
#   return cost[i]

@lru_cache
def rec(i):
  if i == 0:
    return 1
  else:
    return rec(i//2)+rec(i//3)

print(rec(N))

# print((10**9)%2)