grid = []
for i in range(3):
  inp = list(map(int, input().split()))
  grid.append(inp)

# print(grid)
saw = [False]*9
cnt = 0
gakkari = 0

import math

def dfs(i):
  # global cnt
  global gakkari
  saw[i] = True
  # all_saw = True
  # for n in range(9):
  #   if not saw[n]:
  #     all_saw = False
  #     break
  # if all_saw:
  #   cnt += 1
  if check_gakkari(saw, i):
    gakkari += math.factorial(9-dep)
    return

  for j in range(9):
    if not saw[j]:
      dfs(j)
      saw[j] = False

for i in range(9):
  saw = [False]*9
  dfs(i)

print(cnt)