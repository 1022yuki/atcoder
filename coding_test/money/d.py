N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
num = 1
for i in range(N):
    num*=A[i]

while True:
    if num%K==0:
        ans+=1
        num = num//K
    else:
        break

print(ans)