N = int(input())
ps = [0] + list(map(int, input().split()))

maxs = sum(ps)

# exist[i][s]:iまでの問題で得点合計をsにできる
exist = []
for i in range(0, N+1):
  exist.append([False]*(maxs+1))

# 初期条件
exist[0][0] = True

# iの小さい方から順にexitの値を求めていく
for i in range(1, N+1):
  for s in range(0, maxs+1):
    # 問題iを解く場合
    if ps[i] <= s and exist[i-1][s-ps[i]]:
      exist[i][s] = True

    # 問題iを解かない場合
    if exist[i-1][s]:
      exist[i][s] = True

# 答えはexist[N]の中のTrueの個数
count = 0
for j in range(0, maxs+1):
  if exist[N][j]:
    count += 1

print(count)