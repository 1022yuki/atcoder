N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# print(A)

start = 0
for i in range(1, N):
  if A[i]-A[i-1]>1:
    start = i

all_sum = sum(A)
ans = all_sum

tmp = 0
for i in range(N):
  now = (start+i) % N
  if (A[now] - A[(now-1)%N])%M > 1:
    ans = min(ans, all_sum-tmp)
    tmp = 0
  tmp += A[now]

ans = min(ans, all_sum-tmp)
print(ans)