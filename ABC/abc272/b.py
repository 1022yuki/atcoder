N, M = list(map(int, input().split()))

man = []
for i in range(M):
  inp = list(map(int, input().split()))
  k = inp[0]
  x_li = inp[1:]
  man.append(x_li)

grid = []
for i in range(N):
  grid.append([False]*N)

for m in range(M):
  buto = man[m]
  leng = len(buto)
  for i in range(leng):
    for j in range(i+1, leng):
      # print(i, j)
      man1 = buto[i]
      man2 = buto[j]
      grid[man1-1][man2-1] = True

state = True
for i in range(N-1):
  for j in range(i+1, N):
    # print(i, j)
    if not grid[i][j]:
      state = False

if state:
  print('Yes')
else:
  print('No')