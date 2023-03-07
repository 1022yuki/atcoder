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

theta = math.atan((2*B)/A-math.sqrt(3))
x = A/math.cos(theta)
print(x)
exit()