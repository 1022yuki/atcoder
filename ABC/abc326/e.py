N = int(input())
A = list(map(int, input().split()))

# 期待値DP
MOD = 998244353

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

# dp[n]: ますの番号がnのときのA[i]の和の期待値
sal = [-1]*(N+1)
sal[0] = 0

done = [False]*(N+1)
done[0] = True

def rec(n):
  if done[n]:
    return sal[n]
  else:
    done[n] = True
    sal[n] = 0
    for i in range(1, N+1):
      if n-i>=0:
        sal[n] += (rec(n-i)+A[i-1])*power(N, MOD-2, MOD)
        sal[n] %= MOD
    # sal[n] += A[n-1]
    # sal[n] %= MOD
    return sal[n]

rec(N)
print(sal)

ans = 0
for n in range(1, N+1):
  # ますnにいて、n以下を出す確率
  ans += sal[n]*n*power(N, MOD-2, MOD)
  ans %= MOD

print(ans)