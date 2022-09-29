N, A, B = map(int, input().split())

X = []

for i in range(0, A*N):
  X.append([])

# Xを埋める
for i in range(0, A*N):
  for j in range(0, B*N):

    # i//Aが偶数のとき
    if (i//A) % 2 == 0:
      # j//Bが偶数ならX[][]="."、奇数ならX[][]="#"
      if (j//B) % 2 == 0:
        X[i].append('.')
      else:
        X[i].append('#')
    else:
      # j//Bが奇数ならX[][]="."、偶数ならX[][]="#"
      if (j//B) % 2 == 0:
        X[i].append('#')
      else:
        X[i].append('.')

# Xを出力する
for i in range(0, A*N):
  for j in range(0, B*N):
    print(X[i][j], end="")
  print()