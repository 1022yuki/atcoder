from collections import deque

N, M = map(int, input().split())

grid = []
for i in range(N):
  grid.append([-1]*N)
grid[0][0] = 0

vec = []

lim = int(M**0.5)
for a in range(lim+1):
  for b in range(a, lim+1):
    if a*a+b*b == M:
      vec.append((a, b))
      vec.append((-a, b))
      vec.append((a, -b))
      vec.append((-a, -b))
      vec.append((b, a))
      vec.append((-b, a))
      vec.append((b, -a))
      vec.append((-b, -a))

s_vec = set(vec)

Q = deque()
Q.append([0, 0])

while(len(Q)>0):
  i, j = Q.popleft()
  for i2, j2 in s_vec:
    # 範囲確認
    if not 0<=i+i2<=N-1:
      continue
    if not 0<=j+j2<=N-1:
      continue
    
    if grid[i+i2][j+j2] == -1:
      grid[i+i2][j+j2] = grid[i][j]+1
      Q.append([i+i2, j+j2])

# print(grid)
for i in range(N):
  for j in range(N):
    print(grid[i][j], end=' ')
  print()