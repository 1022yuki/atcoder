import sys
def input(): return sys.stdin.readline()[:-1]

H, W, N = map(int, input().split())

grid = []
for i in range(H):
    grid.append([0]*W)
for i in range(N):
    a, b = map(int, input().split())
    a-=1
    b-=1
    grid[a][b] = 1

# 2次元累積和っぽい？
sum_g = []
for i in range(H+1):
    sum_g.append([0]*(W+1))

# 二次元累積和
# 横方向
for i in range(H):
    for j in range(W):
        sum_g[i+1][j+1] = sum_g[i+1][j] + grid[i][j]
# 縦方向
for j in range(W):
    for i in range(H):
        sum_g[i+1][j+1] += sum_g[i][j+1]

# print(sum_g)

ans = 0
for i in range(H):
    for j in range(W):
        ok = 0
        ng = min(H-i, W-j)+1
        while abs(ng-ok)>1:
            mid = (ok+ng)//2
            if sum_g[i+mid][j+mid]-sum_g[i][j+mid]-sum_g[i+mid][j]+sum_g[i][j]==0:
                ok = mid
            else:
                ng = mid
        # print(i, j, ok)
        ans +=  ok

print(ans)