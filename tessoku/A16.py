N = int(input())
A = [0] * 2 + list(map(int, input().split()))
B = [0] * 3 + list(map(int, input().split()))

# print(A)
# print(B)

dp = [0] * (N+1)

dp[2] = A[2]

for i in range(3, N+1):
  dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

# print(dp)
print(dp[N])