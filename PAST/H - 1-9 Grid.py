N, M = map(int, input().split())

A = []
for _ in range(N):
  A.append(input())

print(A)

group = []
for _ in range(11):
  group.append([])
for i in range(N):
  for j in range(M):
    if A[i][j] == "S":
      num = 0
    elif A[i][j] == "G":
      num = 10
    else:
      num = int(A[i][j])
    group[num].append([i, j])

print(group)

# cost[i][j]: 数字を正しく通って、マス[i][j]にたどり着く最小移動回数
cost = []
INF = 10**100
for _ in range(N):
  cost.append([INF]*M)

cost[group[0][0][0]][group[0][0][1]] = 0

# print(cost)

# 数字が小さいマスから順番に埋める
for i in range(1, 11):
  for indaft in group[i]:
    xaft = indaft[0]
    yaft = indaft[1]
    for indbfr in group[i-1]:
      xbfr = indbfr[0]
      ybfr = indbfr[1]

      dx = abs(xaft-xbfr)
      dy = abs(yaft-ybfr)
      dist = dx + dy

      cost[xaft][yaft] = min(cost[xaft][yaft], cost[xbfr][ybfr]+dist)

# print(cost[group[10][0][0]][group[10][0][1]])

if cost[group[10][0][0]][group[10][0][1]] == INF:
  cost[group[10][0][0]][group[10][0][1]] = -1

print(cost[group[10][0][0]][group[10][0][1]])