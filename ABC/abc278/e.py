from collections import defaultdict
H, W, N, h, w = map(int, input().split())

grid = []
for i in range(H):
  inp = list(map(int, input().split()))
  grid.append(inp)

# g_sum_pre[i]: gridの数がiの時1、i以外の時0
g_sum_pre = []
for num in range(1, N+1):
  grid_pre = []
  for i in range(H):
    grid_pre.append([0]*W)
  for i in range(H):
    for j in range(W):
      if grid[i][j] == num:
        grid_pre[i][j]+=1
  g_sum_pre.append(grid_pre)

# for i in range(N):
#   print(g_sum_pre[i])


g_sum_N = []
for i in range(N):
  gr = []
  for i in range(H+1):
    gr.append([0]*(W+1))
  g_sum_N.append(gr)

for n in range(N):
  # 横方向累積和
  for i in range(1, H+1):
    for j in range(1, W+1):
      g_sum_N[n][i][j] = g_sum_N[n][i][j-1] + g_sum_pre[n][i-1][j-1]

  # 縦方向累積和
  for j in range(1, W+1):
    for i in range(1, H+1):
      g_sum_N[n][i][j] = g_sum_N[n][i-1][j] + g_sum_N[n][i][j]

# for i in range(N):
#   print(g_sum_N[i])
  

dic = defaultdict(int)
for i in range(H):
  for j in range(W):
    num = grid[i][j]
    dic[num]+=1

# print(dic)

for i in range(H-h+1):
  ans_li = []
  for j in range(W-w+1):
    # print(i,j)
    # print(i+h, j+w)
    dic_cul = dic.copy()
    for n in range(1, N+1):
      sum = g_sum_N[n-1][i+h][j+w]+g_sum_N[n-1][i][j]-g_sum_N[n-1][i][j+w]-g_sum_N[n-1][i+h][j]
      # print(sum)
      dic_cul[n] -= sum
    
    # print(dic_cul)

    ans = 0
    for val in dic_cul.values():
      if val >= 1:
        ans += 1

    ans_li.append(ans)
  print(*ans_li)