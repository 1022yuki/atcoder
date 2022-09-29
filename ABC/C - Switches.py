N, M = map(int, input().split())

co_num = []
SW = []
for i in range(M):
  inp = list(map(int, input().split()))
  co_num.append(inp[0])
  SW.append(inp[1:])

P = list(map(int, input().split()))

def has_bit(n, i):
  return n&(1<<i) > 0

# スイッチのon,offの全ての組み合わせ
ALL = 1<<N

count = 0

for n in range(ALL):
  switch = [False]*N
  # nが表すスイッチの状態
  for i in range(N):
    if has_bit(n, i):
      switch[i] = True
  
  # print(switch)
  
  # print(switch)
  state = False

  # 各電球について、点灯しているかどうか確認。点灯していなかったら次のループへ
  for m in range(M):
    # その電球が接続しているスイッチのうち、onになっているものの数
    num = 0
    con = SW[m]
    for x in con:
      x -= 1
      if switch[x]:
        num += 1
    if num % 2 != P[m]:
      # 電球mは点灯していない
      state = True
      break
    
  if state:
    continue
  
  # print(n)
  # 全ての電球がonだったら、countに1たす
  count += 1

print(count)