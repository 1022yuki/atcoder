N, Q = map(int, input().split())

# FalseのN×Nの二次元配列を作る
graph = []
for i in range(0, N):
  row = []
  for j in range(0, N):
    row.append(False)

  graph.append(row)

# Q個の操作を受け取る
for i in range(0, Q):
  query = list(map(int, input().split()))

  # フォロー
  if query[0] == 1:
    graph[query[1]-1][query[2]-1] = True

  # フォロー全返し
  if query[0] == 2:
    for i in range(0, N):
      if graph[i][query[1]-1]:
        graph[query[1]-1][i] = True

  #フォローフォロー
  if query[0] == 3:
    # for i in range(0, N):
    #   if graph[query[1]-1][i]:
    #     for j in range(0, N):
    #       if graph[i][j] and j != query[1]-1:
    #         graph[query[1]-1][j] = True

    to_follow = []
    # 全ての頂点を順番に見る
    for i in range(0,N):
      # 頂点aから頂点iへ辺があるとき
      if graph[query[1]-1][i]:
        # 頂点iから頂点jに辺があるかどうか調べ、あるならto_followにjを記録する
        for j in range(0, N):
          if graph[i][j] and j != query[1]-1:
            to_follow.append(j)
    
    # 頂点aから辺を張る
    for i in to_follow:
     graph[query[1]-1][i] = True


# print(graph)

# graphのTrueを'Y'に、Falseを'N'の変換した隣接行列を出力
for i in range(0, N):
  for j in range(0, N):
    # iからjへ辺があるならYを出力、ないならNを出力、改行はしない
    if graph[i][j]:
      print('Y', end='')
    else:
      print('N', end='')
  # 改行
  print()