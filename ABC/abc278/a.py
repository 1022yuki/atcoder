N, K = map(int, input().split())
A = list(map(int, input().split()))

if K <= N:
  ans = A[K:]+[0]*K
else:
  ans = [0]*N

print(*ans)