N = int(input())
A = list(map(int, input().split()))

# i日の塊の生産量
V = [0]*(N+1)

# i日までの生産量の最大値
dp = [0]*(N+1)

for i in range(2, N+1):
  # i日の塊
  V[i] = V[i-1] + A[(i-2)//2]
  for j in range(i, N+1):
    dp[j] = max(dp[j], dp[j-i]+V[i])

# print(V)
print(dp[N])