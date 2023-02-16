N, K, D = map(int, input().split())
A = [0]+list(map(int, input().split()))

dp = []
for i in range(N+1):
  ele = []
  for j in range(K+1):
    ele.append([-1]*D)
  dp.append(ele)
dp[0][0][0] = 0

# print(dp)

for i in range(N):
  for j in range(K+1):
    for d in range(D):
      if dp[i][j][d] == -1:
        continue
      # A[i+1]を選ぶとき
      # j+1がK以下でないといけない
      if j+1<=K:
        dp[i+1][j+1][(d+A[i+1])%D] = max(dp[i+1][j+1][(d+A[i+1])%D], dp[i][j][d]+A[i+1])
      # A[i+1]を選ばないとき
      dp[i+1][j][d] = max(dp[i+1][j][d], dp[i][j][d])

print(dp[N][K][0])