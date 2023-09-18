from collections import deque

C, R = list(map(int, input().split()))
S = []
for i in range(0, R):
  s = list(input().split(" "))
  S.append(s)
# print(S)

for i in range(R):
  for j in range(C):
    if S[i][j]=="s":
      si = i
      sj = j
    if S[i][j]=="g":
      gi = i
      gj = j

# 始点からの移動距離を管理する二次元配列。-1であれば未訪問であることを表す
dist = []
for i in range(0, R):
  dist.append([-1]*C)

# キューを用意して、始点を入れる
Q = deque()
Q.append([si, sj])
dist[si][sj] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
  i, j = Q.popleft()
  #4つの隣マスを確認する
  for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
    # もし盤面の範囲内でなければ無視する
    if not (0 <= i2 < R and 0<= j2 < C):
      continue
    # もし壁マスであれば無視する
    if S[i2][j2] == '1':
      continue
    # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2, j2])

# 始点から終点までの最小移動回数を出力
if dist[gi][gj]!=-1:
  print(dist[gi][gj])
else:
  print('Fail')