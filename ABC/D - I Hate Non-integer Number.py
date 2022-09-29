N = int(input())
A = list(map(int, input().split()))

# 3次元dp
# i個取ることを考える
# dp[j][k][l]: aの左j個からk個選び、和のmodiがlであるような場合の数
# N+1 * N+1 * N

MOD = 998244353

sum = 0

for i in range(1, N+1):

  dp = []
  for a in range(N+1):
    dim2 = []
    for b in range(N+1):
      dim1 = [0]*N
      dim2.append(dim1)
    dp.append(dim2)

  dp[0][0][0] = 1

  for j in range(N):
    for k in range(j+1):
      for l in range(i):
        # ajを選ぶ場合
        newl = (l+A[j]) % i
        dp[j+1][k+1][newl] += dp[j][k][l]

        # 選ばない場合
        dp[j+1][k][l] += dp[j][k][l]
  
  sum += dp[N][i][0] % MOD



print(sum % MOD)