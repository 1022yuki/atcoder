N, M = map(int, input().split())
P = list(map(int, input().split()))

edges = []
for i in range(N):
    edges.append([])

for i in range(N-1):
    edges[P[i]-1].append(i+1)

# print(edges)

dp = [-1] * N

for i in range(M):
    x, y = map(int, input().split())
    dp[x-1] = max(dp[x-1], y)

# print(dp)

for i in range(N):
    st = dp[i]
    for ni in edges[i]:
        dp[ni] = max(dp[ni], st-1)

# print(dp)

ans = 0
for i in range(N):
    if dp[i] >= 0:
        ans += 1

print(ans)