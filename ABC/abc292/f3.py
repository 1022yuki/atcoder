import math

A, B = map(int, input().split())

if A>B:
  c = A
  A = B
  B = c

if B >= 2*A/math.sqrt(3):
  ans = 2*A/math.sqrt(3)
  print(ans)
  exit()

def CulcEdge(theta):
  return A/math.sin((math.pi/6)-theta)

leftDeg = 0
rightDeg = math.pi/6-10**(-10)

while abs(CulcEdge(leftDeg)-CulcEdge(rightDeg))>10**(-9):
  print(leftDeg, rightDeg)
  left_mid = (leftDeg*2+rightDeg)/3
  right_mid = (leftDeg+rightDeg*2)/3
  if CulcEdge(left_mid) > CulcEdge(right_mid):
    rightDeg = right_mid
  else:
    leftDeg = left_mid

print(CulcEdge(rightDeg))