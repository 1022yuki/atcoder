# ビンゴカードの数字を受け取る二次元配列
A = []
for _ in range(3):
  row = list(map(int, input().split()))
  A.append(row)

M = []
for i in range(3):
  row = []
  for j in range(3):
    row.append(False)
  M.append(row)

N = int(input())

# 二次元配列Aの各要素(A[i][j])と各bが一致しているか確認、一致していたらM[i][j]をTrueに変更
for _ in range(0, N):
  b = int(input())
  for i in range(0, 3):
    for j in range(0, 3):
      if A[i][j] == b:
        M[i][j] = True

# ビンゴを達成しているかどうかを記録する変数
bingo = False

#二次元配列Mについてビンゴを達成しているか確認する
# i行目
for i in range(0, 3):
  if M[i][0] and M[i][1] and M[i][2]:
    bingo = True

# j列目
for j in range(0, 3):
  if M[0][j] and M[1][j] and M [2][j]:
    bingo = True

# 斜め
if M[0][0] and M[1][1] and M[2][2]:
  bingo = True

if M[0][2] and M[1][1] and M[2][0]:
  bingo = True

# print(A)
# print(N)
# print(M)

if bingo:
  print('Yes')
else:
  print('No')
