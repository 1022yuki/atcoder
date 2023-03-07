N, X = map(int, input().split())

A = [0]
B = [0]
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

sum = [0]
for i in range(1, N+1):
  sum.append(sum[-1]+A[i]+B[i])
# print(sum)

if X<N:
  N = X
ans = 10**30
for i in range(1, N+1):
  time = sum[i]+B[i]*(X-i)
  ans = min(ans, time)

print(ans)