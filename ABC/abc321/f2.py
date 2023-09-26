import sys
def input(): return sys.stdin.readline()[:-1]

Q, K = map(int, input().split())

qs = []
for _ in range(Q):
    inp = list(map(str, input().split()))
    qs.append(inp)

MOD = 998244353
INF = 10**4

dp = []
for i in range(Q+1):
    dp.append([0]*(K+1))
dp[0][0] = 1

for i in range(Q):
    query = qs[i]
    num = int(query[1])
    if query[0] == "+":
        for j in range(K+1):
            dp[i+1][j] += dp[i][j]
            if j-num >= 0:
                dp[i+1][j] += dp[i][j-num]
    else:
        for j in range(K+1):
            dp[i+1][j] += dp[i][j]
            if j-num >= 0:
                dp[i+1][j] -= dp[i][j-num]
                # if dp[i+1][j] < 0:
                #     dp[i+1][j] = 0
    print(dp[i+1])