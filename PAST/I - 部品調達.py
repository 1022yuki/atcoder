N, M = map(int, input().split())
S = []
C = []
for i in range(M):
  s, c = input().split()
  s_val = 0
  for j in range(N):
    if s[j] == 'Y':
      s_val += 1<<(N-j-1)
  S.append(s_val)
  C.append(int(c))

# print(S)
# print(C)

# cost[i][j]: セットiまで見て、jで表される集合により表現される部品が揃っている場合に必要な金額の最小値
ALL = 1<<N
inf = 10**100
cost = []
for i in range(M+1):
  cost.append([inf]*ALL)

# print(cost)

cost[0][0] = 0

for i in range(M):
  for j in range(ALL):
    # i+1番目の品物を選ぶとき
    cost[i+1][j|S[i]] = min(cost[i+1][j|S[i]], cost[i][j] + C[i])
    # 選ばないとき
    cost[i+1][j] = min(cost[i+1][j], cost[i][j])

# print(cost)
ans = cost[M][ALL-1]
if ans == inf:
  ans = -1

print(ans)