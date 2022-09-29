N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 合計販売枚数を記録する変数
sell = 0

# 全種類販売で販売した1種類当たりの枚数
z = 0

# セット販売で販売した1種類当たりの枚数
s = 0

# セット販売対象のCの最小値を記録する変数
min_s_C = 10 ** 9

# セット販売対象でないCの最小値を記録する変数
min_z_C = 10 ** 9

for i in range(0, N):
  if i % 2 == 0:
    min_s_C = min(C[i], min_s_C)
  else:
    min_z_C = min(C[i], min_z_C)


for _ in range(0, Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    x = query[1]-1
    a = query[2]
    
    if x % 2 == 0:
      card_x = C[x] - z - s
    else:
      card_x = C[x] - z
    
    if card_x >= a:
      C[x] -= a
      sell += a

      #セット販売対象だった場合min_s_Cを更新する
      if x % 2 == 0:
        min_s_C = min(C[x], min_s_C)
      else:
        min_z_C = min(C[x], min_z_C)
    

  elif query[0] == 2:
    a = query[1]

    # i%2==0となる全てのiについて、カードiがa枚以上あるかどうか調べる
    # a以上の場合、a枚ずつ売る
    if min_s_C - s - z >= a:
      s += a

  elif query[0] == 3:
    a = query[1]

    # 全てのiについて、カードiがa枚以上あるかどうか調べる
    # a以上の場合,a枚ずつ売る
    if min(min_s_C - s - z, min_z_C - z) >= a:
      z += a

# セット販売した枚数を合算する
for i in range(0, N):
  if i % 2 == 0:
    sell += s

# 全種類販売した枚数を合算する
sell += z * N

print(sell)