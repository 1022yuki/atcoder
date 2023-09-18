N, M = map(int, input().split())

T = []
W = []
S = []
for i in range(M):
  t, w, s = map(int, input().split())
  T.append(t)
  W.append(w)
  S.append(s)

ans = [0]*N

import heapq
Q = []
for i in range(N):
  heapq.heappush(Q, (i))

# 座圧してシミュレーション
for i in range(N):
  t, w, s = T[i], W[i], S[i]

  if len(Q) == 0:
    continue
  top = heapq.heappop(Q)
  ans[top] += W
  