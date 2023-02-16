T = int(input())

# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    # 答えを表す可変長配列
    res = [-1]*2

    # 3√N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # pで2回割れるとき
        if (N//p)%p==0:
          res[0] = p
          res[1] = N//(p**2)
        # pで1回しか割れないとき
        else:
          res[1] = p
          res[0] = int((N//p)**0.5)
        break

    return res


test = []
for i in range(T):
  n = int(input())
  test.append(n)

for i in range(T):
  num = test[i]
  print(*prime_factorize(num))