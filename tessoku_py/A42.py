N, K = map(int, input().split())

A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

ans = -1

# 体力と気力の下限値を設定して条件を満たしたら追加する
for a in range(1, 101):
  for b in range(1, 101):
    player = 0
    for i in range(N):
      t = A[i]
      k = B[i]
      if a<=t<=a+K and b<=k<=b+K:
        player += 1
    ans = max(ans, player)

print(ans)