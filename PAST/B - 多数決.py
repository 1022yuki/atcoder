s = input()

a = int(s.count('a'))
b = int(s.count('b'))
c = int(s.count('c'))

if a>b and a>c:
  print('a')
elif b>c:
  print('b')
else:
  print('c')