import sys
sys.setrecursionlimit(10**9)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

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
# dp[i]: i秒に曲が切り替わる確率
dp = [-1]*(X+1)
dp[0] = 1

st = sum(T)
# 1/N
N_cond = 1*power(N, MOD-2, MOD)


def rec(i):
  global dp
  if dp[i] != -1:
    return dp[i]
  else:
    dp[i] = 0
    for n in range(N):
      if i-T[n]<0:
        continue
      dp[i] += rec(i-T[n])*N_cond
      dp[i] %= MOD
    return dp[i]

# 答えはdp[X-T[0]+1][0]~dp[X]][0]の和
ans = 0
for time in range(X-T[0]+1, X+1):
  if time<0:
    continue
  ans += rec(time)*N_cond
  ans %= MOD

print(ans)