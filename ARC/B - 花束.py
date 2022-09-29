R, B = map(int, input().split())
x, y = map(int, input().split())

# X個の花束が作れるかどうか判定する関数
def check(X):
  remR = R - X
  remB = B - X
  if remR>=0 and remB>=0:
    if remR//(x-1) + remB//(y-1) >= X:
      return True
  return False

ok = 0
ng = 10**18 + 1

while abs(ok-ng) > 1:
  mid = (ok+ng)//2

  if check(mid):
    ok = mid
  else:
    ng = mid

print(ok)