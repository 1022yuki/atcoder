import copy

H, W, K = map(int, input().split())

grid = []
for i in range(H):
  row = list(input())
  grid.append(row)

def count_b(grid):
  cnt = 0
  for i in range(H):
    for j in range(W):
      if grid[i][j] == '#':
        cnt += 1
  return cnt

def has_bit(n, i):
  return n & 1<<i > 0

ans = 0

for n1 in range(2**H):
  for n2 in range(2**W):
    grid2 = copy.deepcopy(grid)
    # print(grid2)
    # print(n1, n2)
    for r in range(H):
      if has_bit(n1, r):
        for j in range(W):
          grid2[r][j] = '$'
    for c in range(W):
      if has_bit(n2, c):
        for i in range(H):
          grid2[i][c] = '$'
    
    # print(grid2)

    if count_b(grid2) == K:
      ans += 1

print(ans)