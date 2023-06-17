# mはmodをとる数
# 行列の積
def mat_mul(a: list, b: list, m: int) -> list:
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= m
    return c

# 行列の累乗
def mat_pow(x: list, n: int, m: int) -> list:
    L = len(x)

    # 単位行列yを用意
    # yを更新してreturnする
    y = [[0] * L for _ in range(L)]
    for i in range(L):
        y[i][i] = 1

    # xはxの2乗,4乗,8乗...と増えていく
    while n > 0:
        if n & 1:
            y = mat_mul(x, y, m)
        x = mat_mul(x, x, m)
        n >>= 1
      
    return y

A, X, M = map(int, input().split())

Am = [[A, 1], [0, 1]]

Am_pow = mat_pow(Am, X-1, M)

ax = Am_pow[0][0]+Am_pow[0][1]
print(ax%M)