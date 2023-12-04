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

def f(i, j: int) -> int:
  res = 0
  res += sum_grid[N][N]*(i//N)*(j//N)
  res += sum_grid[i%N][j%N]
  res += sum_grid[N][j%N]*(i//N)
  res += sum_grid[i%N][N]*(j//N)
  return res

for i in range(Q):
  a, b, c, d = Qs[i]

  right_bottom = f(c+1, d+1)
  left_bottom = f(c+1, b)
  right_top = f(a, d+1)
  left_top = f(a, b)

  print(right_bottom-left_bottom-right_top+left_top)