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
    edges[b].append(a)


def dfs(i, cnt):
    if cnt == N:
        print(i+1)
        exit()
    for j in edges[i]:
        if not visited[j]:
            cnt += 1
            visited[i] = True
            dfs(j, cnt)
            visited[j] = False
            cnt -= 1

for i in range(N):
    visited = [False]*N
    visited[i] = True
    dfs(i, 1)

print(-1)