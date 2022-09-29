M, N = map(int, input().split())
K = int(input())
grid = []
for i in range(M):
  grid.append(list(input()))

expl = []
for i in range(K):
  a, b, c, d = map(int, input().split())
  expl.append([a, b, c, d])

sum_j = []
sum_o = []
sum_i = []
for i in range(M+1):
  sum_j.append([0]*(N+1))
  sum_o.append([0]*(N+1))
  sum_i.append([0]*(N+1))

# 横方向累積和
for i in range(1, M+1):
  for j in range(1, N+1):
    if grid[i-1][j-1] == 'J':
      sum_j[i][j] = sum_j[i][j-1] + 1
    else:
      sum_j[i][j] = sum_j[i][j-1]
    if grid[i-1][j-1] == 'O':
      sum_o[i][j] = sum_o[i][j-1] + 1
    else:
      sum_o[i][j] = sum_o[i][j-1]
    if grid[i-1][j-1] == 'I':
      sum_i[i][j] = sum_i[i][j-1] + 1
    else:
      sum_i[i][j] = sum_i[i][j-1]

# 縦方向累積和
for j in range(1, N+1):
  for i in range(1, M+1):
    sum_j[i][j] += sum_j[i-1][j]
    sum_o[i][j] += sum_o[i-1][j]
    sum_i[i][j] += sum_i[i-1][j]

# print(sum_j)

for a, b, c, d in expl:
  ans_j = sum_j[c][d] - sum_j[c][b-1] - sum_j[a-1][d] + sum_j[a-1][b-1]
  ans_o = sum_o[c][d] - sum_o[c][b-1] - sum_o[a-1][d] + sum_o[a-1][b-1]
  ans_i = sum_i[c][d] - sum_i[c][b-1] - sum_i[a-1][d] + sum_i[a-1][b-1]
  print(ans_j, ans_o, ans_i)