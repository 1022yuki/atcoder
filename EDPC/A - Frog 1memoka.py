# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N = int(input())
H = list(map(int, input().split()))

cost = [0] * N
done = [False] * N

# メモ化再帰の実装
def rec(i):
  if not done[i]:
    if i >= 2:
      cost[i] = min(rec(i-1)+abs(H[i]-H[i-1]), rec(i-2)+abs(H[i]-H[i-2]))
    elif i == 1:
      cost[i] = rec(i-1) + abs(H[i]-H[i-1])
    else:
      cost[i] = 0
  
  done[i] = True
  return cost[i]

print(rec(N-1))