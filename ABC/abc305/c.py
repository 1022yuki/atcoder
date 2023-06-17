H, W = map(int, input().split())

grid = []
for i in range(H):
    grid.append(list(input()))

# print(grid)

# for i in range(H):
#     flag = False
#     for j in range(W):
#         if grid[i][j] == '#':
#             flag = True
#         if flag and grid[i][j] == '.':
#             print(i+1, j+1)

ans = [0, (-1, -1)]

for i in range(H):
    for j in range(W):
        cnt = 0
        if grid[i][j] == '.':
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                    cnt += 1
            # print(cnt)
            if cnt >= 2:
                # print(i+1, j+1)
                if ans[0] < cnt:
                    ans[0] = cnt
                    ans[1] = (i+1, j+1)

print(*ans[1])