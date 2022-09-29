import heapq

N, M = map(int, input().split())

G = []
for _ in range(0, N):
  G.append([])

for _ in range(0, M):
  u, v, c = map(int, input().split())
  G[u].append((v, c))
  G[v].append((u, c))

# プリム法で最小全域木問題を解く

# 最少全域木の重見に合計を保持する変数
sum = 0

# 頂点iがマークされているかどうかを管理する配列
marked = [False] * N

# マークされている頂点の数を保持する変数
# この値がNになったら終了する
marked_count = 0

marked[0] = True
marked_count += 1

# 次に選ぶ辺の候補を入れるヒープ
Q = []


# 初期条件(頂点0の情報)
for j, c in G[0]:
  heapq.heappush(Q, (c, j))

# 全ての頂点がマークされるまで繰り返す
while marked_count < N:
  c, i = heapq.heappop(Q)

  if marked[i]:
    continue

  marked[i] = True
  marked_count += 1

  sum += c

  # 頂点iに隣接する辺を調べる
  for j, c in G[i]:

    if marked[j]:
      continue

    heapq.heappush(Q, (c, j))

print(sum)