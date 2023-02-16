N = int(input())
A = list(map(int, input().split()))
S = []
for i in range(N):
  s = list(input())
  S.append(s)
Q = int(input())
U = []
V = []
for i in range(Q):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  U.append(u)
  V.append(v)

# ワーシャルフロイドを管理する配列
inf = 10**5
dist = []
for i in range(N):
  dist.append([inf]*N)
# 初期化
for i in range(N):
  dist[i][i] = 0

# 価値を管理
val = []
for i in range(N):
  val.append([-inf]*N)
for i in range(N):
  val[i][i] = A[i]

# 直通(与えられた)経路を追加(重みは1)
for i in range(N):
  for j in range(N):
    if S[i][j] == "Y":
      dist[i][j] = 1
      val[i][j] = val[i][i]+A[j]

# ワーシャルフロイドの計算
for k in range(N):
  for x in range(N):
    for y in range(N):
      if dist[x][y] > dist[x][k]+dist[k][y]:
        # 更新
        dist[x][y] = dist[x][k]+dist[k][y]
        val[x][y] = val[x][k]+val[k][y]-A[k]
      elif dist[x][y] == dist[x][k]+dist[k][y]:
        val[x][y] = max(val[x][y], val[x][k]+val[k][y]-A[k])

# 答えを出力
for i in range(Q):
  u = U[i]
  v = V[i]
  if dist[u][v] == inf:
    print("Impossible")
  else:
    print(str(dist[u][v])+" "+str(val[u][v]))