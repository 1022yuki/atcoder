N = int(input())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))

# print(A)

# cost[n][i]: それまで訪れた都市の集合(を表す整数)がnで、現在都市iにいる時の移動コストの最小値
ALL = 1<<N
inf = 10**100
cost = []
for i in range(ALL):
  cost.append([inf]*N)

cost[0][0] = 0

def has_bit(n, i):
  return ((n&(1<<i)) > 0)

for n in range(ALL):
  # 都市iから都市jへの遷移コストを全て計算
  for i in range(N):
    if not has_bit(n, i):
      if n != 0:
        continue
    for j in range(N):
      if has_bit(n, j) or i==j:
        continue
      cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i]+A[i][j])

# print(cost)
print(cost[ALL-1][0])


# 集合nにiが含まれていて、i==jなら集合nにjも含まれているはずなので、条件i==jは不要なのでは？
# →なぜか結果(dp配列 costの中身)が違う
# →のに、どっちもACになる
# →？？？

# そもそもi==jのときは、同じ点に直接遷移することを意味しているので、A[i][i]=0という本問題の条件のもとではi==jという条件があろうがなかろうが同じ結果になるのでは？