H, W = map(int, input().split()) 

grid = []
for i in range(H):
  s = input()
  grid.append(s)

ans = []

for i in range(H):
  for j in range(W):
    if grid[i][j]=="s":
      if 0<=i+1<=H-1 and 0<=j+1<=W-1 and grid[i+1][j+1]=="n":
        if 0<=i+2<=H-1 and 0<=j+2<=W-1 and grid[i+2][j+2]=="u":
          if 0<=i+3<=H-1 and 0<=j+3<=W-1 and grid[i+3][j+3]=="k":
            if 0<=i+4<=H-1 and 0<=j+4<=W-1 and grid[i+4][j+4]=="e":
              ans.append([[i, j], [i+1, j+1], [i+2, j+2], [i+3, j+3], [i+4, j+4]])
      if 0<=i+1<=H-1 and 0<=j<=W-1 and grid[i+1][j]=="n":
        if 0<=i+2<=H-1 and 0<=j<=W-1 and grid[i+2][j]=="u":
          if 0<=i+3<=H-1 and 0<=j<=W-1 and grid[i+3][j]=="k":
            if 0<=i+4<=H-1 and 0<=j<=W-1 and grid[i+4][j]=="e":
              ans.append([[i, j], [i+1, j], [i+2, j], [i+3, j], [i+4, j]])
      if 0<=i+1<=H-1 and 0<=j-1<=W-1 and grid[i+1][j-1]=="n":
        if 0<=i+2<=H-1 and 0<=j-2<=W-1 and grid[i+2][j-2]=="u":
          if 0<=i+3<=H-1 and 0<=j-3<=W-1 and grid[i+3][j-3]=="k":
            if 0<=i+4<=H-1 and 0<=j-4<=W-1 and grid[i+4][j-4]=="e":
              ans.append([[i, j], [i+1, j-1], [i+2, j-2], [i+3, j-3], [i+4, j-4]])
      if 0<=i<=H-1 and 0<=j-1<=W-1 and grid[i][j-1]=="n":
        if 0<=i<=H-1 and 0<=j-2<=W-1 and grid[i][j-2]=="u":
          if 0<=i<=H-1 and 0<=j-3<=W-1 and grid[i][j-3]=="k":
            if 0<=i<=H-1 and 0<=j-4<=W-1 and grid[i][j-4]=="e":
              ans.append([[i, j], [i, j-1], [i, j-2], [i, j-3], [i, j-4]])
      if 0<=i-1<=H-1 and 0<=j-1<=W-1 and grid[i-1][j-1]=="n":
        if 0<=i-2<=H-1 and 0<=j-2<=W-1 and grid[i-2][j-2]=="u":
          if 0<=i-3<=H-1 and 0<=j-3<=W-1 and grid[i-3][j-3]=="k":
            if 0<=i-4<=H-1 and 0<=j-4<=W-1 and grid[i-4][j-4]=="e":
              ans.append([[i, j], [i-1, j-1], [i-2, j-2], [i-3, j-3], [i-4, j-4]])
      if 0<=i-1<=H-1 and 0<=j<=W-1 and grid[i-1][j]=="n":
        if 0<=i-2<=H-1 and 0<=j<=W-1 and grid[i-2][j]=="u":
          if 0<=i-3<=H-1 and 0<=j<=W-1 and grid[i-3][j]=="k":
            if 0<=i-4<=H-1 and 0<=j<=W-1 and grid[i-4][j]=="e":
              ans.append([[i, j], [i-1, j], [i-2, j], [i-3, j], [i-4, j]])
      if 0<=i-1<=H-1 and 0<=j+1<=W-1 and grid[i-1][j+1]=="n":
        if 0<=i-2<=H-1 and 0<=j+2<=W-1 and grid[i-2][j+2]=="u":
          if 0<=i-3<=H-1 and 0<=j+3<=W-1 and grid[i-3][j+3]=="k":
            if 0<=i-4<=H-1 and 0<=j+4<=W-1 and grid[i-4][j+4]=="e":
              ans.append([[i, j], [i-1, j+1], [i-2, j+2], [i-3, j+3], [i-4, j+4]])
      if 0<=i<=H-1 and 0<=j+1<=W-1 and grid[i][j+1]=="n":
        if 0<=i<=H-1 and 0<=j+2<=W-1  and grid[i][j+2]=="u":
          if 0<=i<=H-1 and 0<=j+3<=W-1 and grid[i][j+3]=="k":
            if 0<=i<=H-1 and 0<=j+4<=W-1 and grid[i][j+4]=="e":
              ans.append([[i, j], [i, j+1], [i, j+2], [i, j+3], [i, j+4]])

# print(ans)

for i in range(len(ans)):
  print(ans[i][0][0]+1, ans[i][0][1]+1)
  print(ans[i][1][0]+1, ans[i][1][1]+1)
  print(ans[i][2][0]+1, ans[i][2][1]+1)
  print(ans[i][3][0]+1, ans[i][3][1]+1)
  print(ans[i][4][0]+1, ans[i][4][1]+1)