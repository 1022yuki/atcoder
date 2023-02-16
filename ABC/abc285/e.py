N = int(input())
A = list(map(int, input().split()))

inf = 10**13
# dp[i][j]: 曜日iでj日平日が連続しているときの生産量の最大値
dp = []
for i in range(N):
  dp.append([-inf]*N)
dp[0][0] = 0

for i in range(1, N):
  for j in range(N):
    # 曜日iを平日にするとき
    if j != 0:
      dp[i][j] = max(dp[i][j], dp[i-1][j-1]+A[(j-1)//2])
    #  曜日iを休日にするとき
    dp[i][0] = max(dp[i][0], dp[i-1][j])

print(max(dp[N-1]))