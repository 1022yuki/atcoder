H, W = map(int, input().split())

grid = []
for i in range(H):
    inp = list(input())
    grid.append(inp)

print(grid)

row = []
col = []

from collections import defaultdict

for i in range(H):
    dict_row = defaultdict(int)
    for j in range(W):
        dict_row[grid[i][j]]+=1
    row.append(dict_row)

print(row)

for i in range(W):
    dict_col = defaultdict(int)
    for j in range(H):
        dict_col[grid[j][i]]+=1
    col.append(dict_col)

print(col)

flag_row = [False] * H
flag_col = [False] * W
deleted_row_num = 0
deleted_col_num = 0
# deleted_row_chr = [0]*26
# deleted_col_chr = [0]*26


upd_flg = True
while upd_flg:
    upd_flg = False
    # 行を削除するか
    for i in range(H):
        if flag_row[i]:
            continue
        for char in range(26):
            # print(row[i][chr(char+97)])
            if row[i][chr(char+97)] == W-deleted_col_num:
                flag_row[i] = True
                deleted_row_num += 1
                upd_flg = True
                break
    # 列を削除するか
    for j in range(W):
        if flag_col[j]:
            continue
        for char in range(26):
            if col[j][chr(char+97)] == H-deleted_row_num:
                flag_col[j] = True
                deleted_col_num += 1
                upd_flg = True
                break   

print(flag_row)
print(flag_col)