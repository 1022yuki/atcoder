A, B, X = map(int, input().split())

ok = 0
ng = 10 ** 9 + 1

while abs(ok-ng)>1:
  mid = (ok+ng)//2

  dig = len(str(mid))

  price = A*mid+B*dig

  if X >= price:
    ok = mid
  else:
    ng = mid

print(ok)