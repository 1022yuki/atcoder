H, W = map(int, input().split())

grid = []
for i in range(H):
  s = list(input())
  grid.append(s)

ans = [0]*W

for i in range(H):
  for j in range(W):
    if grid[i][j]=="#":
      ans[j]+=1

print(*ans)