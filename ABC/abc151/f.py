N = int(input())

X = []
Y = []

for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

# 2点間の距離を返す
def dist(x1, y1, x2, y2):
  dx = x1-x2
  dy = y1-y2
  dist = (dx*dx+dy*dy)**0.5
  return dist

# 点(s, t)を中心とするすべての点を包むような円の半径の最小値を返す
# 要は一番遠い点との距離
def f(s, t):
  ans = -10**5
  for i in range(N):
    x, y = X[i], Y[i]
    ans = max(ans, dist(s, t, x, y))
  return ans

# xについて三分探索し、fが最小になるxを返す
def TernarySearchX():
  left = -1
  right = 1001
  while abs(right-left)>10**(-10):
    # print(left, right)
    cl = (left*2+right)/3
    cr = (left+right*2)/3
    if f(cl, TernarySearchY(cl)) <= f(cr, TernarySearchY(cr)):
      right = cr
    else:
      left = cl
  return f(right, TernarySearchY(right))

# xが決まったとき、yについて三分探索し、fが最小になるyを返す
def TernarySearchY(x):
  left = -1
  right = 1001
  while abs(right-left)>10**(-10):
    cl = (left*2+right)/3
    cr = (left+right*2)/3
    if f(x, cl) <= f(x, cr):
      right = cr
    else:
      left = cl
  return right

print(TernarySearchX())