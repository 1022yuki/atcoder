N, M, Q = map(int, input().split())

# FalseのN×Nの2次元配列を作る

graph = []
for i in range(0, N):
  row = []
  for j in range(0, N):
    row.append(False)
  graph.append(row)

# M本の辺を受け取る
for i in range(0, M):
  u, v = map(int, input().split())

  u -= 1
  v -= 1

  graph[u][v] = True
  graph[v][u] = True

# 頂点の色のリストを受け取る
C = list(map(int, input().split()))

# Q個のクエリを受け取る
for i in range(0, Q):
  query = list(map(int, input().split()))

  # スプリンクラーを起動するクエリ
  if query[0] == 1:
    x = query[1]
    x -= 1
    print(C[x])

    for i in range(0,N):
      if graph[x][i]:
        # 頂点iの色をC[x]に置き換える
        C[i] = C[x]

  # スプリンクラーを起動しないクエリ
  if query[0] == 2:
    x = query[1]
    y = query[2]
    x -= 1
    # 頂点xの色を出力
    print(C[x])
    # 頂点xの色をyに書き換える
    C[x] = y


