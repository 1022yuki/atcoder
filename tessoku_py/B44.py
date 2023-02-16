N = int(input())

grid = []
for i in range(N):
  a = list(map(int, input().split()))
  grid.append(a)

Q = int(input())
queries = []
for i in range(Q):
  n, x, y = map(int, input().split())
  queries.append([n, x, y])

# i行目には元々T[i]行目だった行が入っている
T = []
for i in range(N+1):
  T.append(i)

for q in range(Q):
  n, x, y = queries[q]
  if n == 1:
    t = T[x]
    T[x] = T[y]
    T[y] = t
  if n == 2:
    print(grid[T[x]-1][y-1])