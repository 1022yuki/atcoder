N = int(input())

ans = 10**18

def f(a, b):
  return a*a*a + a*a*b + a*b*b + b*b*b

for a in range(10**6+1):
  ng = -1
  ok = 10**6+1
  while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if f(a, mid) >= N:
      ok = mid
    else:
      ng = mid
    # print(ng, ok)
  ans = min(ans, f(a, ok))

print(ans)