from collections import deque
R, C = map(int, input().split())
si, sj = map(int, input().split())
gi, gj = map(int, input().split())

si -= 1
sj -= 1
gi -= 1
gj -= 1
 
grid = []
for i in range(R):
  grid.append(list(input()))

dist = []
for i in range(R):
  dist.append([-1]*C)
dist[si][sj] = 0

print(dist)

Q = deque()
Q.append([si, sj])

while len(Q)>0:
  i, j = Q.popleft()
  for i2, j2 in [[i+1,j], [i-1, j], [i, j+1], [i, j-1]]:
    if not (0<=i2<R and 0 <=j2<C):
      continue
    if grid[i2][j2] == '#':
      continue
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2, j2])

print(dist[gi][gj])