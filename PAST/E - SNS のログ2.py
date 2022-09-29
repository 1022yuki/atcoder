N, Q = map(int, input().split())

# FalseのN×Nの2次元配列を作る
graph = []
for i in range(0, N):
  row = []
  for j in range(0, N):
    row.append(False)
  graph.append(row)

# 以下、クエリの処理

for i in range(0, Q):
  query = list(map(int, input().split()))

  a = query[1] - 1

  #フォロー
  if query[0] == 1:
    b = query[2] - 1
    graph[a][b] = True

  # フォロー全返し
  if query[0] == 2:
    for j in range(0, N):
      if graph[j][a] and j != a:
        graph[a][j] = True

  # フォローフォロー
  if query[0] == 3:
    # for j in range(0, N):
    #   for k in range(0, N):
    #     if graph[a][j] and j != a:
    #       if graph[j][k] and j != k:
    #         graph[a][k] = True

    # 対象を記録するリスト
    to_follow = []
    
    for j in range(0, N):
      if graph[a][j]:
        for k in range(0, N):
          if graph[j][k] and k != a:
            to_follow.append(k)
    
    for x in to_follow:
      graph[a][x] = True

# print(graph)

# 隣接行列を所望の形式で出力
for i in range(0, N):
  for j in range(0, N):

    if graph[i][j]:
      print("Y", end="")
    else:
      print("N", end="")

  print()