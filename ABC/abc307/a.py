N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    sum = A[7*i]+A[7*i+1]+A[7*i+2]+A[7*i+3]+A[7*i+4]+A[7*i+5]+A[7*i+6]
    ans.append(sum)

print(*ans)