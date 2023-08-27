N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

import bisect

ng = -1
ok = 10**9+1

while abs(ok-ng)>1:
    mid = (ok+ng)//2
    sell = bisect.bisect_right(A, mid)
    buy = M-bisect.bisect_left(B, mid)
    if sell>=buy:
        ok = mid
    else:
        ng = mid

print(ok)
# print(ng)