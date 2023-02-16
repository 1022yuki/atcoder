from collections import deque

T = int(input())

def solve():
  N, M = map(int, input().split())
  C = list(map(int, input().split()))
  edges = []
  for i in range(N):
    edges.append([])
  for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

  visited = []
  for i in range(N):
    visited.append([-1]*N)
  visited[0][N-1] = 0
  
  Q = deque()
  Q.append([0, N-1])

  while len(Q)>0:
    t, a = Q.popleft()
    for nt in edges[t]:
      for na in edges[a]:
        if visited[nt][na] != -1:
          continue
        if C[nt] == C[na]:
          continue
        visited[nt][na] = visited[t][a] + 1
        Q.append([nt, na])
  
  return visited[N-1][0]

ans = []
for t in range(T):
  print(solve())