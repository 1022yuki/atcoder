N = int(input())

# カードの残り枚数を記録する配列
C = list(map(int, input().split()))

Q = int(input())

# 単品販売で売れた枚数を記録する変数
tan = 0

# セット販売で売れた枚数を記録する変数
s = 0
# 全種類販売で売れた枚数を記録する変数
z = 0

# セット販売対象のカードで、単品販売のぶんを引いたものの最小値。真の最小値はmin_s_C-s-zとなる
min_s_C = 1000000000
# セット販売対象でないカードで、単品販売のぶんを引いたものの最小値。真の最小値はmin_s_C-zとなる
min_z_C = 1000000000


# min_s_C,min_z_Cの初期値を求める
for i in range(0, N):
  if i % 2 == 0:
    min_s_C = min(C[i], min_s_C)
  else:
    min_z_C = min(C[i], min_z_C) 


# セット販売を行った1カードあたりの枚数をsと置く解法
# 全種類販売を行った1カードあたりの枚数をz
for i in range(0, Q):

  query = list(map(int, input().split()))


  # 単品販売
  if query[0] == 1:
    x = query[1] - 1
    a = query[2]

    # カードの残っている枚数を計算する
    if x % 2 == 0:
      # セット販売対象カードの場合
      card_x = C[x] - s - z
    else:
      # セット販売対象カードでない場合
      card_x = C[x] - z

    if card_x >= a:
      C[x] -= a
      tan += a
    
    # セット販売対象だった場合min_s_Cを更新する
    if x % 2 == 0:
      min_s_C = min(C[x], min_s_C)
      # 計算量O(1)
    # セット販売対象でなかった場合min_z_Cを更新する
    else:
      min_z_C = min(C[x], min_z_C)


  # セット販売
  if query[0] == 2:
    a = query[1]

    # セット販売可能か
    # 販売可能だった場合
    if min_s_C - s >= a:
      s += a


  # 全種類販売
  if query[0] == 3:
    a = query[1]

    if min(min_z_C - z, min_s_C - s - z) >= a:
      z += a


setto = 0
for i in range(0, N):
  if i % 2 == 0:
    setto += s

zen = z * N

sum = tan + setto + zen






  # # 単品販売
  # if query[0] == 1:

  #   # カード番号とCのindex番号を揃える
  #   x = query[1] - 1

  #   a = query[2]

  #   if C[x] >= a:
  #     C[x] -= a
  #     sum += a

  # # セット販売
  # if query[0] == 2:

  #   a = query[1]
  #   # 番号が奇数であるカードの残り枚数を記録する配列
  #   # 番号が奇数のカード1,3,...,2n+1のindex番号は0,2,...,2n, 
  #   odd = []
  #   for i in range(0, N):
  #     if i % 2 == 0:
  #       odd.append(C[i])

  #   if min(odd) >= a:
  #     for j in range(0, N):
  #       if j % 2 == 0:
  #         C[j] -= a
  #         sum += a


  # # 全種類販売
  # if query[0] == 3:
    
  #   a = query[1]
  #   if min(C) >= a:
  #     for i in range(0, N):
  #       x -= a
  #       sum += a


print(sum)