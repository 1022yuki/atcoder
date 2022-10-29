N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [10**10] * (N+1)
dp[1] = 0

for i in range(1, N):
  if i <= N-1:
    dp[i+1] = min(dp[i+1], dp[i]+A[i-1])
  if i <= N-2:
    dp[i+2] = min(dp[i+2], dp[i]+B[i-1])

print(dp[-1])