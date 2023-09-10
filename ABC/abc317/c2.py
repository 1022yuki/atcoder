import sys
def input(): return sys.stdin.readline()[:-1]
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

N, M = map(int, input().split())

edges = []
for i in range(N):
    edges.append([])

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

ans = -1

def dfs(i, dist):
    global ans
    ans = max(ans, dist)
    for j, c in edges[i]:
        if not visited[j]:
            visited[j] = True
            dist += c
            dfs(j, dist)
            visited[j] = False
            dist -= c

for i in range(N):
    visited = [False]*N
    visited[i] = True
    dfs(i, 0)

print(ans)