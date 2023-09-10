N, X, Y = map(int, input().split())

P = []
T = []
for i in range(N-1):
  p, t = map(int, input().split())
  P.append(p)
  T.append(t)

Qs = []
Q = int(input())
for i in range(Q):
  q = int(input())
  Qs.append(q)

C = []
# 840の周期
for n in range(840):
  cnt_sec = n
  for i in range(N-1):
    if cnt_sec%P[i] != 0:
      cnt_sec += P[i]-(cnt_sec%P[i])
    cnt_sec += T[i]
  # 最初のn秒を2重でカウントしてしまうのでnを引く
  cnt_sec -= n
  C.append(cnt_sec)

for i in range(Q):
  query = Qs[i]
  query += X
  m = query % 840
  query += C[m]
  query += Y
  print(query)