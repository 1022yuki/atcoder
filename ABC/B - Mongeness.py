H, W = map(int, input().split())

A = []

for i in range(0, H):
  row = list(map(int, input().split()))
  A.append(row)

state = True

for i1 in range(1, H):
  for i2 in range(i1+1, H+1):
    for j1 in range(1, W):
      for j2 in range(j1+1, W+1):
        if not A[i1-1][j1-1]+A[i2-1][j2-1] <= A[i2-1][j1-1]+A[i1-1][j2-1]:
          state = False

if state:
  print('Yes')
else:
  print('No')