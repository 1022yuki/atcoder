N = int(input())

# AはN-1xNの配列
A = []
for i in range(N-1):
  lst = list(map(int, input().split()))
  A.append([0]*(i+1) + lst)

print(A)

# ALLは2^Nと同じ
ALL = 1<<N

# ALL種類の集合それぞれに対応する幸福度
happy = [0]*ALL

# nで表される集合に要素iが含まれているかを判定
def has_bit(n, i):
  return (n & 1<<i) > 0

# 2^N要素の配列happyをあらかじめ埋めておく
# happy[n]はnで表現される集合の幸福度を表す
for n in range(ALL):
  for i in range(N):
    for j in range(i+1, N):
      if has_bit(n,i) and has_bit(n, j):
        happy[n] += A[i][j]

ans = -10**10

for n1 in range(ALL):
  for n2 in range(ALL):
    if n1&n2 > 0:
      continue
    # ALL-1 は全ての桁が1, すなわち集合全体
    # n1|n2 は和集合
    n3 = ALL-1 - (n1|n2)
    sum = happy[n1] + happy[n2] + happy[n3]
    ans = max(ans, sum)

print(ans)