R, C = map(int, input().split())

grid = []
for i in range(R):
  inp = list(input())
  grid.append(inp)

b_num = 0
B_pos_pow = []
for i in range(R):
  for j in range(C):
    if grid[i][j] != "#" and grid[i][j] != ".":
      b_num += 1
      B_pos_pow.append([i, j, int(grid[i][j])])

def dist(x1, y1, x2, y2):
  return abs(x1-x2)+abs(y1-y2)

for i in range(R):
  for j in range(C):
    if grid[i][j] == "#":
      for bomb in range(b_num):
        bi, bj, power =  B_pos_pow[bomb]
        if dist(i, j, bi, bj) <= power:
          grid[i][j] = "."
          continue
    if grid[i][j] != "." and grid[i][j] != "#":
      grid[i][j] = "."

# print(B_pos_pow)
# print(grid)

for i in range(C):
  for j in range(R):
    print(grid[i][j], end="")
  print()