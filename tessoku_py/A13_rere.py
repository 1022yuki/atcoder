N, K = map(int, input().split())
A = [0]+list(map(int, input().split()))

R = [0]*N

for i in range(1, N):
  if i==1:
    R[1]=1
  else:
    R[i] = R[i-1]
  
  # whileの条件の順番注意
  while R[i]<N and A[R[i]+1]-A[i]<=K:
    R[i]+=1
  
# print(A)
# print(R)

ans = 0
for i in range(1, N):
  ans += R[i]-i

print(ans)