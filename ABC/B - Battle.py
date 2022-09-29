a, b, c, d = list(map(int, input().split()))

while a>0 and c>0:
  c -= b
  a -= d
  if c<=0 and a<=0:
    print('Yes')
  elif c<=0:
    print('Yes')
  elif a<=0:
    print('No')

