N = int(input())

g1 = []
g2 = []

for i in range(N):
  inp = list(map(int, input().split()))
  g1.append(inp)
for i in range(N):
  inp = list(map(int, input().split()))
  g2.append(inp)

g3 = []
for i in range(N):
  g3.append([0]*N)

import copy

def rot():
  global g1
  global g2
  global g3
  flag = True
  for i in range(N):
    for j in range(N):
      if g1[i][j]==1:
        if g2[i][j]==0:
          flag = False
  # print(g1)
  # print(g2)
  # print()
  for i in range(N):
    for j in range(N):
      g3[N-1-j][i] = g1[i][j]
  # print()
  # print(g1)
  # print()
  # print(g3)
  g1 = copy.deepcopy(g3)
  return flag

for i in range(4):
  if rot():
    print('Yes')
    exit()

print('No')