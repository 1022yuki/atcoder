import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

N, M, K = map(int, input().split())

Es = []
for i in range(M):
  u, v, w = map(int, input().split())
  u -= 1
  v -= 1
  Es.append([u, v, w])

import itertools

Cs = list(itertools.combinations(range(M), N-1))
# print(Cs)

def dfs(i):
  if visited[i]:
    return
  visited[i] = True
  for j in edges[i]:
    if not visited[j]:
      dfs(j)

ans = 10**16

for i in range(len(Cs)):
  wSum = 0
  edgesNums = Cs[i]
  edges = []
  visited = [False]*N
  for j in range(N):
    edges.append([])
  for j in range(len(edgesNums)):
    u, v, w = Es[edgesNums[j]]
    edges[u].append(v)
    edges[v].append(u)
    wSum += w
    wSum %= K
  # print(i)
  # print(edges)
  # print(visited)
  dfs(0)
  # print(visited)
  isAllVisited = True
  for j in range(N):
    if not visited[j]:
      isAllVisited = False
      break
  if isAllVisited:
    # print(wSum)
    ans = min(ans, wSum)

print(ans)