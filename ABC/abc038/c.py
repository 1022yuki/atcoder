N = int(input())
A = [0]+list(map(int, input().split()))

R = [0]*(N+1)
ans = 0

for i in range(1, N+1):
    R[i] = max(i, R[i-1])
    while R[i]<N and A[R[i]+1]>A[R[i]]:
        R[i]+=1
    ans+=R[i]-i+1
# print(R)
print(ans)