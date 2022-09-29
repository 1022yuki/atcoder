N, Q = map(int, input().split())

ball = []

for i in range(N):
  ball.append(i+1)


# iがball[]の何番目にあるかを格納する配列
number = [0]
for i in range(N):
  number.append(i)

# print(ball)
# print(number)


for i in range(0, Q):
  
    # xiを受け取る
    xi = int(input())

    # ball[posi]にxiのボールがある、つまりball[posi]を入れ替える
    posi = number[xi]

    # xiのボールが右端だったとき
    if posi == N-1:
      # xiのボールが右端だったとき、左隣のボールと入れ替える
      # ball[j]とball[j-1]を入れ替える
      # 入れ替えたらfor文を抜け、次のxiへ
      ball[posi], ball[posi-1] = ball[posi-1], ball[posi]
      # numberを更新する。ball[posi], ball[posi-1]が入れ替わっていることに注意
      number[ball[posi]] += 1
      number[ball[posi-1]] -= 1

    # 右端じゃなかったとき
    else:
      # 右隣のボールと入れ替える
      # ball[j]とball[j+1]を入れ替える
      # 入れ替えたらfor文を抜け、次のxiへ
      ball[posi], ball[posi+1] = ball[posi+1], ball[posi]
      # numberを更新する
      number[ball[posi]] -= 1
      number[ball[posi+1]] += 1

    # print(ball)
    # print(number)
    # print()

  

    # for j in range(0, N):

    #   # j番目のボールの番号がxiだったとき
    #   if ball[j] == xi:
        
    #     # xiのボールが右端だったとき
    #     if j == N-1:
    #       # xiのボールが右端だったとき、左隣のボールと入れ替える
    #       # ball[j]とball[j-1]を入れ替える
    #       # 入れ替えたらfor文を抜け、次のxiへ
    #       ball[j], ball[j-1] = ball[j-1], ball[j]

    #     # 右端じゃなかったとき
    #     else:
    #       # 右隣のボールと入れ替える
    #       # ball[j]とball[j+1]を入れ替える
    #       # 入れ替えたらfor文を抜け、次のxiへ
    #       ball[j], ball[j+1] = ball[j+1], ball[j]
        
    #     break

for i in range(N):
  print(ball[i], end=' ')
print()