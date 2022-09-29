N, X = map(int, input().split())
A = list(map(int, input().split()))

right = N
left = -1

while abs(right-left)>1:
  mid = (right+left)//2
  if A[mid] <= X:
    left = mid
  else:
    right = mid

print(right)