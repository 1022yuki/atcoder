n, l = map(float, input().split())
n = int(n)

A = []
B = []
C = []
D = []
for i in range(n):
    a, b, c, d = map(float, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 上下左右の壁のうち、(左, 右), (左, 下)がつながるとアウト
# Unionfindで繋げていく？
# 柵の接続の判定方法


print('YES')