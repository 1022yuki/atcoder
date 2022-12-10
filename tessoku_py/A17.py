N = int(input())
A = [0]*2 + list(map(int, input().split()))
B = [0]*3 + list(map(int, input().split()))

dp = [10**10]*(N+1)
dp[1] = 0

for i in range(2, N+1):
  if i>=3:
    dp[i] = min(dp[i], dp[i-2]+B[i])
  dp[i] = min(dp[i], dp[i-1]+A[i])

# print(dp)

now = N
ans = [N]

while now>1:
  if dp[now] == dp[now-2]+B[now] and now>=3:
    now -= 2
  else:
    now -= 1
  ans.append(now)

ans.reverse()

print(len(ans))
print(*ans)