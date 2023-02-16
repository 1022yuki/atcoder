N = int(input())
A = list(map(int, input().split()))

ans = -1
for i in range(N):
  for j in range(i+1, N):
    b1 = A[i]
    b2 = A[j]
    cond = b1+b2
    min(ans, cond)

print(ans)