N, M = map(int, input().split())
from collections import deque
import sys
sys.setrecursionlimit(10**9)

visited = [False]*N
visited_rev = [False]*N
Q = deque()

A = []
B = []
edges = []
edges_rev = []
for i in range(N):
    edges.append([])
    edges_rev.append([])

for i in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    edges[b].append(a)
    edges_rev[a].append(b)

def dfs(i, num):
    visited[i] = True
    visnum[i] = num
    for j in edges[i]:
        if not visited[j]:
            dfs(j, num+1)

for i in range(N):
    visited = [False]*N
    visnum = [0]*N
    dfs(i, 0)
    if visited.count(True) == N:
        # print('aaaaaa')
        for i in range(N):
            if visnum[i] == N-1:
                print(i+1)
                exit()

print(-1)