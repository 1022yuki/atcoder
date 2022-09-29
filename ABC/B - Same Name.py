N = int(input())

NAME = []
for i in range(0, N):
  row = list(map(str, input().split()))
  NAME.append(row)

value = False

for i in range(0, N):
  for j in range(0, N):
    if NAME[i][0] == NAME[j][0] and NAME[i][1] == NAME[j][1] and i != j:
      value = True

if value:
  print('Yes')
else:
  print('No')