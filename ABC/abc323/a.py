S = input()

flag = True
for i in range(2, 17):
  if i % 2 == 1:
    continue
  if S[i-1] != '0':
    flag = False
    break

if flag:
  print('Yes')
else:
  print('No')