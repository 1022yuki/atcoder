N, K = map(int, input().split())
H = list(map(int, input().split()))

cost = [0]*N
cost[0] = 0

# K個目の足場まで
# KがN以上の場合,インデックスがはみ出すのでi=N-1で止める
for i in range(1, K+1):
  if K>=N and i==N:
    break
  c_li = []
  for j in range(0, i):
    c_li.append(cost[j] + abs(H[i]-H[j]))
    cost[i] = min(c_li)

# K+1個目の足場から
# まずはこの動作が必要がどうか場合分け
if K+1 <= N:
  for i in range(K, N):
    c_li = []
    for j in range(1, K+1):
      c_li.append(cost[i-j] + abs(H[i]-H[i-j]))
      cost[i] = min(c_li)

print(cost[-1])