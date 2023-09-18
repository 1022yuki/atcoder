N, M = map(int, input().split())
import sys
sys.setrecursionlimit(10**9)

edges = []
for i in range(N):
    edges.append([])

for i in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)

visited = [False]*N

def dfs(i):
    visited[i] = True
    for j in edges[i]:
        if not visited[j]:
            dfs(j)

# print(edges)

for i in range(N):
    visited = [False]*N
    dfs(i)
    if visited.count(True) == N:
        print(i+1)
        exit()

# print(visited)
print(-1)