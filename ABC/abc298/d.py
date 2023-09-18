N, x, y = map(int, input().split())
A = list(map(int, input().split()))

li_x = [False]*(2*(10**4)+1)
li_y = [False]*(2*(10**4)+1)
li_x[0+A[0]+10**4] = True
li_y[0+10**4] = True

for i in range(1, N):
  li = [False]*(2*(10**4)+1)
  if i%2==0:
    for j in range(2*(10**4)+1):
      if li_x[j]:
        if 0<=j+A[i]<=2*(10**4):
          li[j+A[i]] = True
        if 0<=j-A[i]<=2*(10**4):
          li[j-A[i]] = True
    li_x = li
  else:
    for j in range(2*(10**4)+1):
      if li_y[j]:
        if 0<=j+A[i]<=2*(10**4):
          li[j+A[i]] = True
        if 0<=j-A[i]<=2*(10**4):
          li[j-A[i]] = True
    li_y = li
    
flag_x = False
flag_y = False
if li_x[x+10**4]:
  flag_x = True
if li_y[y+10**4]:
  flag_y = True

if flag_x and flag_y:
  print('Yes')
else:
  print('No')