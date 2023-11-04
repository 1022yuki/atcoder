grid = []
for i in range(9):
  grid.append(list(map(int, input().split())))

flagA = True
flagB = True
flagC = True

# gridの各行に1~9が一つずつあるか確認(順番はなんでも良い)
for i in range(9):
  tmp = [False]*9
  for j in range(9):
    tmp[grid[i][j]-1] = True
  if False in tmp:
    flagA = False
    break

# gridの各列に1~9が一つずつあるか確認(順番はなんでも良い)
for j in range(9):
  tmp = [False]*9
  for i in range(9):
    tmp[grid[i][j]-1] = True
  if False in tmp:
    flagB = False
    break

# gridの各3x3のブロックに1~9が一つずつあるか確認(順番はなんでも良い)
for i in range(3):
  for j in range(3):
    tmp = [False]*9
    for k in range(3):
      for l in range(3):
        tmp[grid[3*i+k][3*j+l]-1] = True
    if False in tmp:
      flagC = False
      break

if flagA and flagB and flagC:
  print('Yes')
else:
  print('No')