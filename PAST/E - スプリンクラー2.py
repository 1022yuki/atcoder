N, M, Q = map(int, input().split())

# FalseのN×Nの二次元配列を作る
# graph = []
# for i in range(0, N):
#   row = []
#   for j in range(0, N):
#     row.append(False)
#   graph.append(row)

# N×0の二次元配列を作る
graph = []

for i in range(0, N):
  # 空の配列をN個作りgraphに追加
  row = []
  graph.append(row)


for i in range(0, M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1

  # 二次元配列graphの[u][v]及び[v][u]をTrueに
  # graph[u][v] = True
  # graph[v][u] = True

  # 受け取ったu,vに対しgraph[u]にvを追加、graph[v]にuを追加
  graph[u].append(v)
  graph[v].append(u)


C = list(map(int, input().split()))

for i in range(0, Q):
  s = list(map(int, input().split()))
  x = s[1] - 1

  # 処理1
  if s[0] == 1:
    print(C[x])
    for j in graph[x]:
      C[j] = C[x]

  # 処理2
  if s[0] == 2:
    print(C[x])
    C[x] = s[2]
