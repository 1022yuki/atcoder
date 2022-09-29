K = int(input())

a, b = map(int, input().split())

pro = False

for i in range(a, b+1):
  if i % K == 0:
    pro = True

if pro:
  print('OK')
else:
  print('NG')