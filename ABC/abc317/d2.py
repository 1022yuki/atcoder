N = int(input())

X = []
Y = []
Z = []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

inf = 10**12
all_seat = sum(Z)
# dp[i][j]: i番目までの選挙区でj議席を獲得するときの最小の鞍替え人数
dp = []
for i in range(N+1):
    dp.append([inf]*(10**5+1))
dp[0][0] = 0

for i in range(N):
    x, y, z = X[i], Y[i], Z[i]
    for j in range(10**5+1):
        if dp[i][j]==inf:
            continue
        if x>y:
            # すでに高橋くんが勝利している
            if j+z<=10**5:
                dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j])
        else:
            # 青木くんが勝利している
            # そのままにしておく
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # 鞍替えさせ議席を獲得する
            # 鞍替えさせる必要がある人数
            change= (y-x)//2+1
            if j+z<=10**5:
                dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j]+change)

need = (all_seat//2)+1
print(min(dp[N][need:]))