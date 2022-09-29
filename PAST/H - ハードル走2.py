N, L = map(int, input().split())
X = list(map(int, input().split()))

hardle = [False]*(L+1)
for x in X:
  hardle[x] = True

T1, T2, T3 = map(int, input().split())

# print(hardle)

cost = [10**10]*(L+1)
cost[0] = 0


# 終点を揃えると、飛んでいるいないもあるので無理,始点で考える
# 座標iにハードルがある場合それも追加し、minをとる(ハードル考慮後に比較するのは飛んでいる可能性もあるため)
for i in range(0, L+1):

  # 行動1
  if i+1 <= L:
    kodo1 = cost[i] + T1
    if hardle[i+1]:
      kodo1 += T3
    cost[i+1] = min(cost[i+1], kodo1)

  # 行動2
  if i+2 <= L:
    kodo2 = cost[i] + T1 + T2
    if hardle[i+2]:
      kodo2 += T3
    cost[i+2] = min(cost[i+2], kodo2)

  # 行動3
  if i+4 <= L:
    kodo3 = cost[i] + T1 + 3*T2
    if hardle[i+4]:
      kodo3 += T3
    cost[i+4] = min(cost[i+4], kodo3)

  # これにて、cost[-1]にはゴール時地面にいる場合の最小値が保存されている

  # cost[-1]と、ゴール時に空中にいる3パターンの最小値が答えである

ans = cost[-1]
if L == 2:
  for i in range(1, 3):
    j_case = cost[-1-i] + T1//2 + (T2*(2*i-1))//2
    ans = min(ans, j_case)
else:
  for i in range(1, 4):
    j_case = cost[-1-i] + T1//2 + (T2*(2*i-1))//2
    ans = min(ans, j_case)

print(ans)

# print(cost)