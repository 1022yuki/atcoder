N = int(input())

ok1 = 0
ng1 = N+1
ok2 = 0
ng2 = N+1

while abs(ng1-ok1)>1:
  mid = (ng1+ok1)//2
  print("?", 1, mid, 1, N, flush=True)
  t = int(input())
  if t == mid:
    ok1 = mid
  else:
    ng1 = mid

while abs(ng2-ok2)>1:
  mid = (ng2+ok2)//2
  print("?", 1, N, 1, mid, flush=True)
  t = int(input())
  if t == mid:
    ok2 = mid
  else:
    ng2 = mid

print("!", ng1, ng2, flush=True)