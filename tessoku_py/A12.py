N, K = map(int, input().split())
A = list(map(int, input().split()))

left = -1
right = 10**9

while abs(right-left)>1:
  mid = (left+right)//2
  sum = 0
  for x in A:
    sum += mid // x
  if sum < K:
    left = mid
  else:
    right = mid

print(right)