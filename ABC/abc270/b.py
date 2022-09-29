X, Y, Z = map(int, input().split())

if Y>0 and Z>Y and X>Y:
  print(-1)
  exit()

if Y<0 and Z<Y and X<Y:
  print(-1)
  exit()

if 0<Y and Y<X and Z<0:
  ans = abs(X)+2*abs(Z)
elif 0>Y and X<Y and Z>0:
  ans = abs(X)+2*abs(Z)
else:
  ans = abs(X)

print(ans)