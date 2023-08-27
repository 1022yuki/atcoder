N, D = map(int, input().split())

X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

edges = []
for i in range(N):
    edges.append([])

for i in range(N):
    for j in range(i+1, N):
        if dist(X[i], Y[i], X[j], Y[j]) <= D:
            edges[i].append(j)
            edges[j].append(i)

import sys
sys.setrecursionlimit(10**9)

visited = [False]*N

def dfs(i):
    visited[i] = True
    for j in edges[i]:
        if not visited[j]:
          dfs(j)

dfs(0)

for i in range(N):
    if visited[i]:
        print('Yes')
    else:
        print('No')