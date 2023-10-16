import sys
sys.setrecursionlimit(10**9)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=0') 

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

# メモ化再帰で解く
# dp[i][j]: i秒に曲jの再生が始まる確率
dp = []
for i in range(X+1):
  dp.append([-1] * N)

st = sum(T)
# dp[0][0]: 0秒で曲jの再生が始まる確率は1/N
s_cond = power(N, MOD-2, MOD)
for j in range(N):
  dp[0][j] = s_cond

def rec(i, j):
  global dp
  if dp[i][j] != -1:
    return dp[i][j]
  else:
    dp[i][j] = 0
    for n in range(N):
      if i-T[n]<0:
        continue
      dp[i][j] += rec(i-T[n], n)*s_cond
      dp[i][j] %= MOD
    return dp[i][j]

# 答えはdp[X-T[0]+1][0]~dp[X]][0]の和
ans = 0
for time in range(X-T[0]+1, X+1):
  ans += rec(time, 0)
  ans %= MOD

print(dp)
print(ans)