X, Y = map(int, input().split('.'))

if 0<=Y<=2:
  print(str(X)+'-')
elif 3<=Y<=6:
  print(X)
else:
  print(str(X)+'+')