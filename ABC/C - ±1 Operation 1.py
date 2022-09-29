X, A, D, N = map(int, input().split())

if D<0:
  A = A + (N-1) * D
  D *= -1

left = A
right = A+(N-1)*D

if X <= left:
  ans = left - X
elif X >= right:
  ans = X - right 
else:
  ans1 = (X-A)%D
  ans2 = D-((X-A)%D)
  # print(ans1, ans2)
  ans = min(ans1, ans2)

print(ans)