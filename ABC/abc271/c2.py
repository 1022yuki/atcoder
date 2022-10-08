N = int(input())
A = list(map(int, input().split()))

set_A = set(A)

# mid巻読めるかで二分探索
ok = 0
ng = N+1


while abs(ng-ok)>1:
  mid = (ok+ng)//2
  cnt_have = len(set(range(1, mid+1)) & set_A)
  all = cnt_have + (N-cnt_have)//2
  if all >= mid:
    ok = mid
  else:
    ng = mid

print(ok)