import sys
sys.setrecursionlimit(10**7)
# def input(): return sys.stdin.readline()[:-1]

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])

for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  edges[u].append(v)

cnt = 0

def dfs(i):
  global cnt
  # print(i+1)
  visited[i] = True
  for j in edges[i]:
    if not visited[j]:
      dfs(j) 
      cnt += 1

for i in range(N):
  visited = [False]*N
  dfs(i)

cnt -= M

print(cnt)