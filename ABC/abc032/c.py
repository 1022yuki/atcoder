N, K = map(int, input().split())

S = [1]
for i in range(N):
    s = int(input())
    S.append(s)

if 0 in S:
    print(N)
    exit()

# print(S)

R = [-1]*(N+1)
R[0] = 1
prod = S[1]

ans = 0
for i in range(1, N+1):
    prod //= S[i-1]
    R[i] = R[i-1]
    if S[i] > K:
        prod = 1
        R[i] = i-1
        # continue
    while R[i]+1<=N and prod*S[R[i]+1]<=K:
        prod *= S[R[i]+1]
        R[i] += 1
    ans = max(ans, R[i]-i+1)

# print(R)
print(ans)