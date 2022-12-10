from collections import deque
H, W = map(int, input().split())

grid = []
for i in range(H):
  grid.append(list(input()))

for i in range(H):
  for j in range(W):
    if grid[i][j] == 'S':
      si, sj = i, j
      grid[i][j] = '#'
      break
    
dist = []
for i in range(H):
  dist.append([-1]*W)

def bfs(si, sj, num):

  Q = deque()
  Q.append([si, sj])

  # キューから取り出しながら探索する
  while len(Q) > 0:
    i, j = Q.popleft()
    dist[i][j] = num
    #4つの隣マスを確認する
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
      # print(i2, j2)
      # もし盤面の範囲内でなければ無視する
      if not (0<=i2<H and 0<=j2<W):
        continue
      # もし壁マスであれば無視する
      if grid[i2][j2] == '#':
        continue
      # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
      if grid[i2][j2] == '.':
        if dist[i2][j2]>0 and dist[i2][j2]!=num:
          print('Yes')
          exit()
        if dist[i2][j2] == -1:
          Q.append([i2, j2])
          dist[i2][j2] = num


st_gl = [[si+1, sj], [si-1, sj], [si, sj+1], [si, sj-1]]

for i in range(4):
  s_i, s_j = st_gl[i]
  if not (0<=s_i<H and 0<=s_j<W):
    continue
  if grid[s_i][s_j] == '#':
    continue
  bfs(s_i, s_j, i+1)


# print(dist)
print('No')