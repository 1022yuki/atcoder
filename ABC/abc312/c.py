N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

import bisect

ok = -1
ng = 10**9+1

while abs(ok-ng)>1:
    mid = (ok+ng)//2
    sell = bisect.bisect_right(A, mid)
    buy = M-bisect.bisect_left(B, mid)
    # print(ok, ng, mid, sell, buy)
    if sell>=buy:
        ng = mid
    else:
        ok = mid

# print(ok)
print(ng)