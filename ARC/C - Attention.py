N = int(input())
S = input()


# 最小人数を保持する変数
min_turn = 3 * 10**5


# 累積和(sum_W[i]はi-1人目までの西向きの人数の累積和)(N+1要素)
# リーダーより西にいて西向きの人の数はsum_W[i]となる
sum_W = [0]
for i in range(0, N):
  if S[i] == "W":
    sum_W.append(sum_W[i] + 1)
  else:
    sum_W.append(sum_W[i])


for i in range(0, N):

  # 人iをリーダーとした時の向きを変える必要がある人数を記録する変数
  turn = 0
  
  # リーダーより西の人が西向きの時
  w = sum_W[i]

  # リーダーより東の人が東向きの時
  e = sum_W[i+1]-sum_W[N]+N-i-1

  turn = w + e

  min_turn = min(min_turn, turn)

print(min_turn)