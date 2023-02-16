N = int(input())

f = 0
a = 0
for i in range(N):
  s = input()
  if s == "For":
    f += 1
  else:
    a += 1

if f>a:
  print('Yes')
else:
  print("No")