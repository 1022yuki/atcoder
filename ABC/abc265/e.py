# from collections import defaultdict

MOD = 998244353

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

# dict = defaultdict(int)
S = set()
for i in range(M):
  x, y = map(str, input().split())
  S.add((x, y))

# print(dict)

dp = []
for i in range(N+1):
  dp_pre = []
  for j in range(N+1):
    dp_pre.append([0]*(N+1))
  dp.append(dp_pre)
dp[0][0][0] = 1

# print(dp)

# (i, j, k)の組み合わせの字ワープ先に障害物があるか判定 あればFalseなければTrue
def is_ok(i, j, k):
  x = A*i+C*j+E*k
  y = B*i+D*j+F*k
  return (x, y) in S

# 3次元のdp配列を埋めていく
for i in range(N):
  for j in range(N):
    for k in range(N):
      if i + j + k >= N:
        continue
      
      # 障害物がなければTrue
      if is_ok(i+1, j, k):
        dp[i+1][j][k] += dp[i][j][k]
        dp[i+1][j][k] %= MOD
      if is_ok(i, j+1, k):
        dp[i][j+1][k] += dp[i][j][k]
        dp[i][j+1][k] %= MOD
      if is_ok(i, j, k+1):
        dp[i][j][k+1] += dp[i][j][k]
        dp[i][j][k+1] %= MOD

# print(dp)

cnt = 0
for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
      if i + j + k == N:
        cnt += dp[i][j][k]
        cnt %= MOD

print(cnt)

# [A, B] = -[C, D] みたいなとき大丈夫なのか？