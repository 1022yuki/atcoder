N, K = map(int, input().split())
h = list(map(int, input().split()))

# cost[i]: 足場iにたどり着くための最小コスト。サイズNを確保する。
cost = [0]*N
cost[0] = 0

if K <= N:
  # 足場0から足場Kまでのコストの最小値をそれぞれ計算、保存
  for i in range(1, K):
    list = []
    for j in range(0, i):
      list.append(cost[j]+abs(h[i]-h[j]))
    cost[i] = min(list)

  # print(cost)

  # 足場K以降はK個のジャンプ元からのコストのうち最小値を保存
  for i in range(K, N):
    list = []
    for k in range(1, K+1):
      list.append(cost[i-k]+abs(h[i]-h[i-k]))
    cost[i] = min(list)

else:
  for i in range(1, N):
    list = []
    for j in range(0, i):
      list.append(cost[j]+abs(h[i]-h[j]))
    cost[i] = min(list)

# print(cost)

print(cost[N-1])