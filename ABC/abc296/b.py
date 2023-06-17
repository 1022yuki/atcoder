grid = []
for i in range(8):
  s = list(input())
  grid.append(s)

for i in range(8):
  for j in range(8):
    if grid[i][j]=="*":
      ti = i
      tj = j
      # break

tjj = chr(ord('a')+tj)
# print(8-ti)
print(str(tjj)+str(8-ti))