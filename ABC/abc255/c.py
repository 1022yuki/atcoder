X, A, D, N = map(int, input().split())

if D < 0:
  A = A + (N-1) * D
  D *= -1

def f(k):
  return A + (k * D)

# A, A+D, A+2D, ...,A+(N-1)D について,k=0~N-1 まで二分探索
left = -1
right = N
while abs(right-left)>1:
  if abs(f(left)-X) >= abs(f(right)-X):
    left = (right+left)//2
  else:
    right = (right+left)//2

# print(left, right)

if left == -1:
  ans1 = abs(f(left+1)-X)
  ans2 = abs(f(left+2)-X)
elif right == N:
  ans1 = abs(f(right-1)-X)
  ans2 = abs(f(right-2)-X)
  
else:
  ans1 = abs(f(left)-X)
  ans2 = abs(f(right)-X)

print(min(ans1, ans2))