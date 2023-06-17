# flagによってYesとNoを出力
def op(flag):
    if flag:
        print('Yes')
        exit()
    # else:
    #     print('No')

H, W = map(int, input().split())

grid = []
for i in range(H):
    inp = list(input())
    grid.append(inp)

# print(grid)

S = [0]*min(H, W)
cent = []

for i in range(H):
    for j in range(W):
        if grid[i][j]=="#":
            if 1<=i<=H-2 and 1<=j<=W-2:
              if grid[i-1][j-1]=="#" and grid[i-1][j+1]=="#" and grid[i+1][j-1]=="#" and grid[i+1][j+1]=="#":
                cent.append([i, j])

# print(cent)

def conti(i, j):
    size = 0
    while(grid[i][j]=="#"):
        # if i==0 or j==0:
        #     break
        i-=1
        j-=1
        size+=1
        if i<0 or j<0:
            break
    return size
    

for i, j in cent:
    S[conti(i, j)-2]+=1

print(*S)