a, b, c = list(map(str, input().split()))

al = len(a)
bl = len(b)

if a[al-1]==b[0] and b[bl-1]==c[0]:
  print('YES')
else:
  print('NO')