N, K = map(int, input().split())
A = list(map(int, input().split()))

def bin_search(n):
  ok = -1
  ng = K
  while abs(ng-ok)>1:
    mid = (ok+ng)//2
    if A[mid] <= n:
      ok = mid
    else:
      ng = mid

  # n -= A[ok]
  return A[ok]

takahashi = 0
aoki = 0
cnt = 0
while N>0:
  if cnt % 2 == 0:
    # print(N)
    ret = bin_search(N)
    takahashi += ret
    N -= ret
  else:
    # print(N)
    ret = bin_search(N)
    aoki += ret
    N -= ret

  cnt += 1

# print(takahashi)