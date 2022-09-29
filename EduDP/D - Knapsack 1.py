N, W = map(int, input().split())

ws = [0]
vs = [0]
for i in range(0, N):
  w, v = map(int, input().split())
  ws.append(w)
  vs.append(v)

# print(ws)
# print(vs)

# value[i][w]: 品物iまで見て重さ合計wであるときの価値の総和の最大値 N+1xW+1
# 小さい値で初期化しておく
# 求めるものはvalue[N][W]
value = []
for i in range(0, N+1):
  value.append([-1]*(W+1))

# print(value)

# 初期条件
value[0][0] = 0

# iが小さい順に求めていく
for i in range(1, N+1):
  for w in range(0, W+1):
    # value[i][w] = max(value[i-1][w], value[i-1][w-ws[i]]+vs[i])

    # 品物iを選ぶ場合
    if w-ws[i] >= 0:
      value[i][w] = max(value[i][w], value[i-1][w-ws[i]]+vs[i])

    # 選ばない場合
    value[i][w] = max(value[i][w], value[i-1][w])

# print()

print(value)

print(max(value[N]))