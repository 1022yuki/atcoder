N, M = map(int, input().split())

grid = []
for i in range(N):
    s = input()
    grid.append(s)

code = [
    '###.?????',
    '###.?????',
    '###.?????',
    '....?????',
    '?????????',
    '?????....',
    '?????.###',
    '?????.###',
    '?????.###'
  ]

for i in range(N-9+1):
    for j in range(M-9+1):
        flag = True
        for ind_i in range(9):
            for ind_j in range(9):
                # print(i, j, ind_i, ind_j)
                if ind_i<4 and ind_j<4 and grid[i+ind_i][j+ind_j]!=code[ind_i][ind_j]:
                    flag = False
                if ind_i>=5 and ind_j>=5 and grid[i+ind_i][j+ind_j]!=code[ind_i][ind_j]:
                    flag = False
        if flag:
          print(i+1, j+1)