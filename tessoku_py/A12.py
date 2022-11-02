N, K = map(int, input().split())
A = list(map(int, input().split()))

left = -1
right = 10**9

while abs(right-left)>1:
  mid = (left+right)//2
  sum = 0
  for i in range(N):
    sum += mid // A[i]
  if sum < K:
    left = mid
  else:
    right = mid

print(right)