N1, N2, M = map(int, input().split())

N = N1+N2
edges = []
for i in range(N):
    edges.append([])

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

from collections import deque
Q1 = deque()
Q2 = deque()
visited1 = [-1]*N
visited2 = [-1]*N
Q1.append(0)
Q2.append(N-1)
visited1[0] = 0
visited2[N-1] = 0

while len(Q1)>0:
    i = Q1.popleft()
    for j in edges[i]:
        if visited1[j]==-1:
            visited1[j]=visited1[i]+1
            Q1.append(j)

while len(Q2)>0:
    i = Q2.popleft()
    for j in edges[i]:
        if visited2[j]==-1:
            visited2[j]=visited2[i]+1
            Q2.append(j)

# print(visited1)
# print(visited2)

v1 = max(visited1)
v2 = max(visited2)

print(v1+v2+1)