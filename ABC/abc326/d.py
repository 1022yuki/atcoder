N = int(input())
R = list(input())
C = list(input())

# N*Nのリストgridを受け取る
def check(grid):
  # グリッドの各行にa,b,cが1つずつあるか
  for i in range(N):
    if grid[i].count('A')!=1 or grid[i].count('B')!=1 or grid[i].count('C')!=1:
      return False
  # グリッドの各列にa,b,cが1つずつあるか
  for j in range(N):
    cntA = 0
    cntB = 0
    cntC = 0
    for i in range(N):
      if grid[i][j]=='A':
        cntA+=1
      elif grid[i][j]=='B':
        cntB+=1
      elif grid[i][j]=='C':
        cntC+=1
    if cntA!=1 or cntB!=1 or cntC!=1:
      return False
  # グリッドのi行目に書かれた文字のうち、最も左にある文字がRのi文字目と一致するか
  mostLeftStr = []
  for i in range(N):
    for j in range(N):
      if grid[i][j]!='.':
        mostLeftStr.append(grid[i][j])
        break
  for i in range(N):
    if mostLeftStr[i]!=R[i]:
      return False
  # グリッドのi列目に書かれた文字のうち、最も上にある文字がCのi文字目と一致するか
  mostUpStr = []
  for j in range(N):
    for i in range(N):
      if grid[i][j]!='.':
        mostUpStr.append(grid[i][j])
        break
  for j in range(N):
    if mostUpStr[j]!=C[j]:
      return False
  return True

# N*Nのgridを作る(3<=N<=5)
# gridの各行にA,B,Cを1つずつ入れる
# そのgridが条件を満たすかどうかをチェックする
# 条件を満たすならば、そのgridを出力する

rows = []
for i in range(3):
  rows.append([])
for a in range(N):
  for b in range(N):
    if a!=b:
      for c in range(N):
        if a!=b and b!=c and c!=a:
          row = ['.']*N
          row[a] = 'A'
          row[b] = 'B'
          row[c] = 'C'
          for i in range(N):
            if row[i]=='A':
              rows[0].append(row)
              break
            if row[i]=='B':
              rows[1].append(row)
              break
            if row[i]=='C':
              rows[2].append(row)
              break

# print(rows)
# print(len(rows))
lr = len(rows[0])

import itertools

# 使用例
combos = itertools.product(range(lr), repeat=N)
# print(*combos)

for combo in combos:
  grid = []
  for n in range(N):
    if R[n]=='A':
      grid.append(rows[0][combo[n]])
    elif R[n]=='B':
      grid.append(rows[1][combo[n]])
    elif R[n]=='C':
      grid.append(rows[2][combo[n]])
  # print(grid)
  if check(grid):
    print('Yes')
    # print(grid)
    for i in range(N):
      print(''.join(grid[i]))
    exit()

print('No')