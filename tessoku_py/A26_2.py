Q = int(input())

dlt = [False]*(300001)

lim1 = int(300000**0.5)

for i in range(2, lim1+1):
  if dlt[i]:
    continue
  lim2 = 300000 // i
  for j in range(2, lim2+1):
    dlt[i*j] = True

inp = []
for i in range(Q):
  inp.append(int(input()))

for num in inp:
  if not dlt[num]:
    print('Yes')
  else:
    print('No')