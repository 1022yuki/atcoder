N, M = map(int, input().split())

grid = []
for i in range(N):
    s = list(input())
    grid.append(s)

for i in range(N-9+1):
    for j in range(M-9+1):
        flag1 = True
        flag2 = True
        for k in range(9):
            for l in range(9):
                if k<3 and l<3 and grid[i+k][j+l]=='.':
                    flag1 = False
                if k>=6 and l>=6 and grid[i+k][j+l]=='.':
                    flag1 = False
                if k==3 and l<4 and grid[i+k][j+l]=='#':
                    flag2 = False
                if k<4 and l==3 and grid[i+k][j+l]=='#':
                    flag2 = False
                if k==5 and l>4 and grid[i+k][j+l]=='#':
                    flag2 = False
                if k>5 and l==5 and grid[i+k][j+l]=='#':
                    flag2 = False
        if flag1 and flag2:
            print(i+1, j+1)