N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

s_b = set(B)

dp = [False]*(X+1)
dp[0] = True
for i in range(1, X+1):
  if i in s_b:
    continue
  for j in range(N):
    if i-A[j]>=0:
      if dp[i-A[j]]:
        dp[i] = True

if dp[-1]:
  print("Yes")
else:
  print("No")