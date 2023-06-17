# https://strangerxxx.hateblo.jp/entry/20220201/1643705539

# 配列aの[l, r)の部分のnext_permutation
def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

# 使い方
n = 3
a = list(range(n))
while True:
    print(a)
    if not next_permutation(a, 0, n):
        break


def prev_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の前の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] > a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

# 使い方
# while True:
#     print(a)
#     if not prev_permutation(a, 0, n):
#         break