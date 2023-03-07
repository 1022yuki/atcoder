import math
A, B = map(int, input().split())

if A>B:
  c = A
  A = B
  B = c

x = (2*A)/math.sqrt(3)
if x <= B:
  print(x)
  exit()



def f(x):
  return A*math.cos(math.pi/6-x)-B*math.cos(x)

ng = 0
ok = math.pi/6
while abs(ok-ng)>10**(-10):
  mid = (ok+ng)/2
  if f(mid)>=0:
    ok = mid
  else:
    ng = mid

# print(ok)

x = A/math.cos(ok)
print(x)