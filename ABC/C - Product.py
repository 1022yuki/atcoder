N, X = map(int, input().split())

# 袋の中身の整数を受け取る配列
A = []
for i in range(0, N):
  A.append([])

for i in range(0, N):
  row = list(map(int, input().split()))
  for j in range(0, row[0]):
    A[i].append(row[j+1])

print(A)

# 動的計画法に用いる配列([N+1][X+1])
# 0で初期化する
dp = []
for i in range(0, N+1):
  dp.append([0]*(X+1))
dp[0][0] = 1

print(dp)

for n in range(0, N):
  for x in range(0, X+1):
    for a in range(0, len(A[n])):
      if x*A[n][a] <= X:
        dp[n+1][x*A[n][a]] += dp[n][x]

print(dp)

print(dp[N][X])