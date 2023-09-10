N = int(input())

edges = []
for i in range(N):
    edges.append([])

C = []
Ps = []
for i in range(N):
    inp = list(map(int, input().split()))
    c = inp[0]
    ps = inp[1:]
    C.append(c)
    Ps.append(ps)

for i in range(N):
    c = C[i]
    ps = Ps[i]
    for j in range(c):
        edges[i].append(ps[j]-1)

visited = [False] * N
visited[0] = True
ans = []

def dfs(i):
    visited[i] = True
    for j in edges[i]:
        if not visited[j]:
            dfs(j)
            ans.append(j+1)

dfs(0)
print(*ans)