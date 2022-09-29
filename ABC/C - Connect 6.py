N = int(input())

grid = []
for i in range(N):
  grid.append(input())

for i in range(N):
  for j in range(N):
    s_i = i
    s_j = j
    if N-j >= 6:
      # 横に見る
      cnt = 0
      # state = False
      for p in range(6):
        if grid[i][j+p] == '.':
          cnt += 1
      if cnt <= 2:
        # state = True
        print('Yes')
        exit()

    if N-i >= 6:
      # 縦にみる
      cnt = 0
      # state = False
      for p in range(6):
        if grid[i+p][j] == '.':
          cnt += 1
      if cnt <= 2:
        # state = True
        print('Yes')
        exit()

    if N-i >= 6 and N-j >= 6:
      # 斜め(右下に進む)に見る
      cnt = 0
      # state = False
      for p in range(6):
        if grid[i+p][j+p] == '.':
          cnt += 1
      if cnt <= 2:
        # state = True
        print('Yes')
        exit()

    if N-i >= 6 and j >= 5:
      # 斜め(右上に進む)に見る
      cnt = 0
      # state = False
      for p in range(6):
        if grid[i+p][j-p] == '.':
          cnt += 1
      if cnt <= 2:
        # state = True
        print('Yes')
        exit()

print('No')