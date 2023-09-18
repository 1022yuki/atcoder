N = int(input())
S = input()

f1 = False
f2 = True

for s in S:
  if s=="o":
    f1 = True
  if s=="x":
    f2 = False

if f1 and f2:
  print('Yes')
else:
  print('No')