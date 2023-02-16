N = int(input())
A = list(map(int, input().split()))

taro = []
jiro = []
for i in range(N-1):
  taro.append([0]*N)
  jiro.append([0]*N)
taro.append(A)
jiro.append(A)

# dp[i][j][p]: (i,j)まで進行しp=0(太郎くん) p=1(次郎くん)のときどのように行動するか
dp = []
for i in range(N):
  dp.append([[0, 0]]*(N-1))

print(dp)