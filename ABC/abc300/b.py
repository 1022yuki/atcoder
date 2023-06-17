# flagによってYesとNoを出力
def op(flag):
    if flag:
        print('Yes')
        exit()
    # else:
    #     print('No')

H, W = map(int, input().split())

ga = []
gb = []

for i in range(H):
    inp = list(input())
    ga.append(inp)

for i in range(H):
    inp = list(input())
    gb.append(inp)

# print(ga)
# print(gb)



for i in range(H):
    # 縦シフト
    c = ga[-1]
    ga.pop()
    ga = [c]+ga
    # print(ga)
    for j in range(W):
        # 横シフト
        for k in range(H):
            rot = ga[k]
            ap = rot.pop()
            ga[k] = [ap]+rot
        # print(ga)
        op(ga==gb)
print('No')