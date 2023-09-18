A, B, D = map(int, input().split())
C = list(map(int, input().split()))
X, Y, Z = map(int, input().split())

# 方針
# ステップ1: i日目に必要になるカードリッジの数を求める
# ステップ2: dpでi日目に購入を行うかどうかの遷移についてコストの最小値を求める

# ステップ1
sup = []
sup.append([B]*A)
for i in range(D):
    sup.append([0]*A)

daily_need = []
for d in range(1, D+1):
    sum = 0
    for j in range(A):
        sup[d][j] = sup[d-1][j] - C[j]
        # 最終日前日にちょうど使い切った場合は補充する必要はない
        if d==D and abs(sup[d][j])%B==0:
            num = (abs(sup[d][j])//B)
            sum += num
            sup[d][j] += num*B
        elif sup[d][j] <= 0:
            num = (abs(sup[d][j])//B)+1
            sum += num
            sup[d][j] += num*B
    daily_need.append(sum)

print(sup)
print(daily_need)

# ステップ2
dp = []
for i in range(D+1):
    dp.append([10**10]*(D+1))
dp[0][0] = 0

for i in range(D):
    for j in range(i+1):
      if daily_need[i]==0:
         dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
      else:
        # i+1日目に購入を行う場合
        dp[i+1][0] = min(dp[i+1][0], dp[i][j]+(daily_need[i]*X)+Y)
        # i+1日目に購入を行わない場合
        # 1度も購入していない場合この動作は行えない
        if i!=j:
          dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+(daily_need[i]*X)+Z*(j+1))

ans = min(dp[D])
print(ans)