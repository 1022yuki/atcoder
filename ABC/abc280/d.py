# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    # 答えを表す可変長配列
    res = []

    # √N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p

        # 答えに追加
        res.append((p, e))

    # 素数が最後に残ることがありうる
    if N != 1:
        res.append((N, 1))

    return res

import math
K = int(input())

bunkai = prime_factorize(K)
# print(bunkai)


def check(num):
  for soinsu, ruijo in bunkai:
    # print(soinsu, ruijo)
    ruijo_sum = 0
    div_m = int(math.log(num, soinsu))
    # print(div_m)
    for i in range(1, div_m+1):
      ruijo_sum += num//(soinsu**i)
    if ruijo_sum < ruijo:
      return False
  return True

    
# 二分探索
left = 0
right = 10**12+1

while abs(right-left)>1:
  # print(left, right)
  mid_num = (right+left)//2
  # print(mid_num)
  if check(mid_num):
    right = mid_num
  else:
    left = mid_num

print(right)
# print(left)