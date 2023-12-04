import sys
def input(): return sys.stdin.readline()[:-1]

N, Q = map(int, input().split())

grid = []

for i in range(N):
  grid.append(list(input()))

for i in range(N):
  g_new = []
  for j in range(N):
    if grid[i][j] == "B":
      g_new.append(1)
    else:
      g_new.append(0)
  grid[i] = g_new

Qs = []
for i in range(Q):
  Qs.append(list(map(int, input().split())))

# 二次元累積和
sum_grid = [[0]*(N+1) for i in range(N+1)]

# 横方向に累積和
for i in range(1, N+1):
  for j in range(1, N+1):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

# 縦方向に累積和
for j in range(1, N+1):
  for i in range(1, N+1):
    sum_grid[i][j] += sum_grid[i-1][j]

for i in range(Q):
  a, b, c, d = Qs[i]
  sho_a = a//N
  rem_a = a%N
  sho_b = b//N
  rem_b = b%N
  sho_c = (c+1)//N
  rem_c = (c+1)%N
  sho_d = (d+1)//N
  rem_d = (d+1)%N

  add_migisita = 0
  add_migisita += sum_grid[N][N]*sho_c*sho_d
  add_migisita += sum_grid[rem_c][rem_d]
  add_migisita += sum_grid[N][rem_d]*sho_c
  add_migisita += sum_grid[rem_c][N]*sho_d
  del_hidarisita = 0
  del_hidarisita += sum_grid[N][N]*sho_c*sho_b
  del_hidarisita += sum_grid[rem_c][rem_b]
  del_hidarisita += sum_grid[N][rem_b]*sho_c
  del_hidarisita += sum_grid[rem_c][N]*sho_b
  del_nigiue = 0
  del_nigiue += sum_grid[N][N]*sho_a*sho_d
  del_nigiue += sum_grid[rem_a][rem_d]
  del_nigiue += sum_grid[N][rem_d]*sho_a
  del_nigiue += sum_grid[rem_a][N]*sho_d
  add_hidariue = 0
  add_hidariue += sum_grid[N][N]*sho_a*sho_b
  add_hidariue += sum_grid[rem_a][rem_b]
  add_hidariue += sum_grid[N][rem_b]*sho_a
  add_hidariue += sum_grid[rem_a][N]*sho_b

  print(add_migisita-del_hidarisita-del_nigiue+add_hidariue)