def has_bit(n, i):
  return n & 1<<i > 0

# a の b 乗を m で割った余りを返す関数
def power(a, b, m):
  p = a
  Answer = 1
  # rangeの部分はb<2**rangeになるように調整
  for i in range(30):
    if has_bit(b, i):
      Answer = (Answer*p) % m
    p = (p * p) % m
  return Answer

N, X = map(int, input().split())
T = list(map(int, input().split()))

# 確率dp
MOD = 998244353

# dp[i][j]: i秒に曲jの再生が始まる確率
# dp[i][0]: i秒に曲1の再生が始まる確率
# dp[i][1]: i秒に曲1以外の再生が始まる確率
dp = []
for i in range(N+1):
  dp.append([0] * 2)

st = sum(T)
# dp[0][0]: 0秒で曲1の再生が始まる確率はT[0]/sum(T)
dp[0][0] = (T[0]*power(st, MOD-2, MOD))%MOD
# dp[0][0]: 0秒で曲1の再生が始まる確率は(sum(T)-T[0])/sum(T)
dp[0][1] =  ((st-T[0])*power(st, MOD-2, MOD))%MOD

print(dp)

