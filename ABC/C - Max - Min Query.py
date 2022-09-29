# S = []
count = {}
exist_num = []

max_val = 0
min_val = 10 ** 9

Q = int(input())

for i in range(0, Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    # クエリ1の処理
    x = query[1]    
    # max, minの更新
    max_val = max(max_val, x)
    min_val = min(min_val, x)

    # 辞書countを更新、キーがないときは作って0
    if x not in count:
      count[x] = 0

    # 追加する前のcount[x]が0だったらexist_numに追加
    if count[x] == 0:
      exist_num.append(x)
    
    count[x] += 1

    # print(count)
    # print(exist_num)
    

  if query[0] == 2:
    # クエリ2の処理
    x = query[1]
    c = query[2]

    if x in count:
      del_num = min(c, count[x])
      if del_num == count[x]:
        # exist_numからxを削除, max,minを更新
        exist_num.remove(x)

        if len(exist_num) != 0:
          # exist_numの要素があれば
          max_val = max(exist_num)
          min_val = min(exist_num)
        else:
          # なければ
          max_val = 0
          min_val = 10 ** 9

      count[x] -= del_num
    
    # print(count)
    # print(exist_num)

  if query[0] == 3:
    # クエリ3の処理
    ans = max_val - min_val
    print(ans)

    # print(count)
    # print(exist_num)