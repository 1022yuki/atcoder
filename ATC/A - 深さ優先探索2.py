import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())

map = []

for i in range(H):
  map.append(list(input()))

# print(map)

visited = []
for i in range(H):
  visited.append([False]*W)

for i in range(H):
  for j in range(W):
    if map[i][j] == "s":
      si = i
      sj = j
    if map[i][j] == "g":
      gi = i
      gj = j

def rec(i, j):
  visited[i][j] = True
  next = [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]
  for ni, nj in next:
    if 0<=nj<W and 0<=ni<H:
      if not visited[ni][nj]:
        if map[ni][nj] != "#":
          rec(ni, nj)

rec(si, sj)

# print(visited)

if visited[gi][gj]:
  print('Yes')
else:
  print('No')