import math
from collections import deque

N = int(input())

sx, sy, tx, ty = map(int, input().split())

cir = []
for i in range(N):
  inf = list(map(int, input().split()))
  cir.append(inf)

# print(cir)

# 隣接リストを作成
E = []
for i in range(N):
  E.append([])

for i in range(N):
  for j in range(i+1, N):
    if (cir[i][2]-cir[j][2])**2 <= (cir[i][0]-cir[j][0])**2+(cir[i][1]-cir[j][1])**2 <= (cir[i][2]+cir[j][2])**2:
      E[i].append(j)
      E[j].append(i)

# print(E)


visited = []
for i in range(N):
  visited.append(False)

Q = deque()

for i in range(N):
  if (sx-cir[i][0])**2+(sy-cir[i][1])**2 == (cir[i][2])**2:
    Q.append(i)
    visited[i] = True

for i in range(N):
  if (tx-cir[i][0])**2+(ty-cir[i][1])**2 == (cir[i][2])**2:
    tar = i

while len(Q) > 0:
  i = Q.popleft()
  for j in E[i]:
    if not visited[j]:
      visited[j] = True
      Q.append(j)


if visited[tar]:
  print('Yes')
else:
  print('No')