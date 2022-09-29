N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

grid = []
for i in range(Q-P+1):
  grid.append(['.']*(S-R+1))

# print(grid)

a = max(1-A, 1-B)
b = min(N-A, N-B)
c = max(1-A, B-N)
d = min(N-A, B-1)

# print(a)
# print(b)
# print(c)
# print(d)

for i in range(Q-P+1):
  for j in range(S-R+1):
    ni = P + i
    nj = R + j
    if ni-A == nj-B and a <= ni-A <= b:
      grid[i][j] = '#'
    if ni-A == B-nj and c <= ni-A <= d:
      grid[i][j] = '#'

# print(grid)

for i in range(Q-P+1):
  for j in range(S-R+1):
    print(grid[i][j], end='')
  print()