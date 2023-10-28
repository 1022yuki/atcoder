N = int(input())
D = list(map(int, input().split()))

INF = 10**15

l1, c1, k1 = map(int, input().split())
l2, c2, k2 = map(int, input().split())

# dp[i][j]: i番目の区間まで見て, センサ1をj回使った時のセンサー2の個数の最小値
dp = []
for i in range(N+1):
  dp.append([INF]*(k1+1))

for i in range(k1+1):
  dp[0][i] = 0

for i in range(1, N+1):
  lg = D[i-1]
  for j in range(k1+1):
    if lg%l1==0:
      numSensor1Max = lg//l1
    else:
      numSensor1Max = lg//l1 + 1
    for n1 in range(numSensor1Max+1):
      remLg = max(lg-n1*l1, 0)
      if remLg%l2==0:
        n2 = remLg//l2
      else:
        n2 = remLg//l2 + 1
      if j-n1>=0 and n2<=(k2-dp[i-1][j-n1]):
        dp[i][j] = min(dp[i][j], dp[i-1][j-n1]+n2)

ans = INF
for n1 in range(k1+1):
  ci = c1*n1+c2*dp[N][n1]
  ans = min(ans, ci)

# print(dp)
if ans==INF:
  print(-1)
else:
  print(ans)