N, A, B, C = map(int, input().split())

D = []
for i in range(N):
  D.append(list(map(int, input().split())))

import heapq

# dist[0][i]: i番目の街に行き,まだ電車を使っていないときの最小コスト
# dist[1][i]: i番目の街に行き,既に電車を使っているときの最小コスト
dist = []
for i in range(2):
  dist.append([-1]*N)
dist[0][0] = 0
dist[1][0] = 0

done = []
for i in range(2):
  done.append([False]*N)

Q = []
heapq.heappush(Q, (0, 0, 0)) # (コスト, 街の番号, 電車を使ったかどうか)
heapq.heappush(Q, (0, 0, 1)) # (コスト, 街の番号, 電車を使ったかどうか)

while len(Q)>0:
  d, i, isUsedTrain = heapq.heappop(Q)

  if done[isUsedTrain][i]:
    continue
  done[isUsedTrain][i] = True

  if isUsedTrain==0:
    # 電車を使ってない場合
    # 電車に乗るかそのままかの2つある
    # 電車に乗る場合
    for j in range(N):
      if j==i:
        continue
      if dist[1][j]==-1 or dist[1][j] > d + (D[i][j]*B)+C:
        dist[1][j] = d + (D[i][j]*B)+C
        heapq.heappush(Q, (dist[1][j], j, 1))
    # そのまま車の場合
    for j in range(N):
      if j==i:
        continue
      if dist[0][j]==-1 or dist[0][j] > d + D[i][j]*A:
        dist[0][j] = d + D[i][j]*A
        heapq.heappush(Q, (dist[0][j], j, 0))
  else:
    # 電車を既に使っている場合
    for j in range(N):
      if j==i:
        continue
      if dist[1][j]==-1 or dist[1][j] > d + (D[i][j]*B)+C:
        dist[1][j] = d + (D[i][j]*B)+C
        heapq.heappush(Q, (dist[1][j], j, 1)) 

# print(dist)
ans = min(dist[0][N-1], dist[1][N-1])
print(ans)