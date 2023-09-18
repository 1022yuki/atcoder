from collections import defaultdict

n, l = map(int, input().split())

tate = defaultdict(list)
yoko = defaultdict(list)

    
A = []
B = []
C = []
D = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


for i in range(n):
    a = A[i]
    b = B[i]
    c = C[i]
    d = D[i]
    if a == c:
        # 縦の線
        # b<dにする
        if b>d:
            b, d = d, b
        # 判定
        for y in range(b, d+1):
            for left, right in yoko[y]:
                if left==0 and left<=a<=right:
                    print('No')
                    print(i+1)
                    exit()
        # 線を追加
        tate[a].append([b, d])
            
    if b == d:
        # 横の線
        # a<cにする
        if a>c:
            a, c = c, a
        # 判定
        for x in range(a, c+1):
            for top, bottom in tate[x]:
                if bottom==0 and top<=b<=bottom:
                    print('No')
                    print(i+1)
                    exit()
        # 線を追加
        yoko[b].append([a, c])


print('Yes')