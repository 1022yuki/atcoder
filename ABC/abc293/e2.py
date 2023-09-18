A, X, M = map(int, input().split())

# https://qiita.com/ophhdn/items/e6451ec5983939ecbc5b

# mはmodをとる数
# 行列の積
def mat_mul(a: list, b: list) -> list:
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= M
    return c

# 行列の累乗
def mat_pow(x: list, n: int) -> list:
    L = len(x)

    # 単位行列yを用意
    # yを更新してreturnする
    y = [[0] * L for _ in range(L)]
    for i in range(L):
        y[i][i] = 1

    # xはxの2乗,4乗,8乗...と増えていく
    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1
      
    return y


m_A = [[A, 1], [0, 1]]
m_A_pow = mat_pow(m_A, X-1)

ax = (m_A_pow[0][0]+m_A_pow[0][1])%M
print(ax)