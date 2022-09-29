N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# print(A)
sum_li = [0]
for i in range(N):
  sum_li.append(sum_li[-1]+A[i])
# print(sum_li)

def bin_search(A, x):
  ng = -1
  ok = N
  while(abs(ok-ng)>1):
    mid = (ok+ng)//2
    if A[mid] >= x:
      ok = mid
    else:
      ng = mid

  up_cost = sum_li[-1]-sum_li[ok]-x*(N-ok)
  down_cost = x*ok-sum_li[ok]

  return up_cost+down_cost

for query in range(Q):
  x = int(input())
  print(bin_search(A, x))