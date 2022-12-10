N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
  sum.append(sum[-1]+A[i])

R = [0]*(N+1)

for i in range(1, N+1):
  if i==1:
    R[i] = 0
  else:
    R[i] = R[i-1]
  
  while R[i]<N and sum[R[i]+1]-sum[i-1]<=K:
    R[i] += 1

# print(R)

sum = 0
for i in range(1, N+1):
  sum += R[i]-i+1

print(sum)