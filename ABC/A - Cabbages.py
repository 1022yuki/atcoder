N, A, X, Y = map(int, input().split())

if N > A:
  sum = X*A + Y*(N-A)
else:
  sum = X*N

print(sum)