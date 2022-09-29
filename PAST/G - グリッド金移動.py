from collections import deque

N, X, Y = map(int, input().split())

# X += 200
# Y += 200

# グリッドを表す配列
M = []
for i in range(0, 401):
  row = ["."] * (401)
  M.append(row)

for i in range(0, N):
  x, y = map(int, input().split())
  M[x+200][y+200] = "#"

print(M)


# (0,0)からの移動回数を表す配列,X,Yより大きい部分は無視する
dist = []
for i in range(0, 401):
  row = [-1] * 401
  dist.append(row)

Q = deque()
Q.append([0,0])

dist[0][0] = 0

while len(Q)>0:

  x, y = Q.popleft()

  # print(x)
  # print(y)

  for x2, y2 in [[x+1,y+1], [x,y+1], [x-1,y+1], [x+1,y], [x-1,y], [x, y-1]]:

    # X,Yからはみ出していたら次のループへ
    if X>=0 and x2>X:
      continue

    if X<=0 and x2<X:
      continue

    if Y>=0 and y2>Y:
      continue

    if Y<=0 and y2<Y:
      continue

    # 障害物があったら次のループへ
    if M[x2][y2] == "#":
      continue
    
    # 未訪問なら距離を更新してQに追加
    if dist[x2][y2] == -1:
      dist[x2][y2] = dist[x][y] + 1
      Q.append([x2,y2])


print(dist[X][Y])
# print(M[201][201])