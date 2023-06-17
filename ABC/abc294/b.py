H, W = map(int, input().split())

grid = []
for i in range(H):
  inp = list(map(int, input().split()))
  grid.append(inp)

A = ord("A")
# print(A)

ans = []
for i in range(H):
  ans.append(["."]*W)

for i in range(H):
  for j in range(W):
    if grid[i][j]!=0:
      ans[i][j] = chr(A+grid[i][j]-1)

# print(ans)

for i in range(H):
  print("".join(ans[i]))