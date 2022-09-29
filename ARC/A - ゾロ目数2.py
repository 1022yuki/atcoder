N = int(input())

# 今までに出てきたゾロ目数の数
z = 0

# 1から555555までの整数を全て調べる。調べている数をiとする
# for i in range(1, 555555+1):

#   si = str(i)

#   ok = True

#   for s in si:
#     if s != si[0]:
#       ok = False

#   if ok:
#     z += 1
  
#   if ok and z == N:
#     ans = i

# print(ans)


for i in range(1, 555555+1):

  # iをを文字列に変換
  si = str(i)

  # 変換したsiに含まれる文字が全て同じであるかチェックする
  ok = True

  for x in si:
    if x != si[0]:
      ok = False

  if ok:
    z += 1
  
  if N == z:
    print(i)
    break