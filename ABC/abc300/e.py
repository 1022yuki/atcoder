import sys
sys.setrecursionlimit(10**7)

from collections import defaultdict

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


N = int(input())
mod = 998244353

dic_dp = defaultdict(int)
dic_memo = defaultdict(int)
dic_dp[1] = 1
dic_memo[1] = 1
#  メモ化再帰
# dp[n]: nから出た目で割っていって1になる確率
# dp = [0]*(N+1)
# dp[1] = 1
# flag = [False]*(N+1)
# flag[1] = True

def rec(n):
    if dic_memo[n]==1:
        return dic_dp[n]
    else:
      p2 = 0
      p3 = 0
      p4 = 0
      p5 = 0
      p6 = 0
      if n%2==0:
         p2 = rec(n//2)
      if n%3==0:
         p3 = rec(n//3)
      if n%4==0:
         p4 = rec(n//4)
      if n%5==0:
         p5 = rec(n//5)
      if n%6==0:
         p6 = rec(n//6)
      p = (p2+p3+p4+p5+p6)
      dic_memo[n] = True
      dic_dp[n] = (p*power(5, mod-2, mod))%mod
      return dic_dp[n]

rec(N)
print(dic_dp[N])