N = int(input())
A = list(map(int, input().split()))

edges = []
for i in range(N+1):
    edges.append([])

for i in range(N):
    edges[i+1].append(A[i])

# print(edges)

visited = [False]*(N+1)
inCycleList = [False]*(N+1)
from collections import deque


def dfs(i):
    queue.append(i)
    visited[i] = True
    for j in edges[i]:
        if visited[j]:
            while True:
                inCycle = queue.pop()
                inCycleList[inCycle] = True
                if inCycle == j:
                    break
        else:
            dfs(j)

for i in range(1, N+1):
    queue = deque()
    visited = [False]*(N+1)
    if not visited[i]:
        dfs(i)

# print(inCycleList)

ans = inCycleList.count(True)
print(ans)