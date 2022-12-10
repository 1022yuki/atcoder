from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

N = int(input())

# 隣接グラフ(連想配列)
edges = defaultdict(list)

for i in range(N):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

# print(edges)

visited = defaultdict(bool)


ans = 1
def dfs(i):
  global ans
  visited[i] = True
  ans = max(ans, i)
  for j in edges[i]:
    if not visited[j]:
      dfs(j)

dfs(1)

# print(visited)
print(ans)