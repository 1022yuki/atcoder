N = int(input())

wl = []

for i in range(N):
  wl.append(list(input()))

# print(wl)

state = True

for i in range(N):
  for j in range(i+1):
    if wl[i][j] == 'W' and wl[j][i] != 'L':
      state = False

    if wl[i][j] == 'L' and wl[j][i] != 'W':
      state = False
    
    if wl[i][j] == 'D' and wl[j][i] != 'D':
      state = False

if state:
  print('correct')
else:
  print('incorrect')