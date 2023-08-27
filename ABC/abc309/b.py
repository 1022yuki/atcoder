N = int(input())

grid = []
for i in range(N):
    grid.append(list(input()))

ans = []

for i in range(N):
    if i==0:
        ans.append([grid[i+1][0]]+grid[0][:-1])
    elif i==N-1:
        ans.append(grid[i][1:]+[grid[i-1][-1]])
    else:
        ans.append([grid[i+1][0]]+grid[i][1:-1]+[grid[i-1][-1]])

# print(ans)
# print()
for i in range(N):
    print(''.join(ans[i]))