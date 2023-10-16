xa, ya, xb, yb, xc, yc = map(int, input().split())

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# x座標を先に揃える場合
ans1 = 0
# 荷物と目的地のx座標を揃える
if xc-xb!=0:
    # 自分が荷物の右側にいて、目的地も荷物の右側にある場合
    if xa-xb>0 and xc-xb>0:
        # 荷物の左側に移動して、荷物のx座標を目的地のx座標に揃える
        ans1 += (manhattan(xa, ya, xb-1, yb)+manhattan(xc, yb, xc, yc))
        # y座標が最初から同じ場合は+2
        if ya==yb:
            ans1 += 2
    # 自分が荷物の右側にいて、目的地が荷物の左側にある場合
    if xa-xb>0 and xc-xb<0:
        # 荷物の右側に移動して、荷物のx座標を目的地のx座標に揃える
        ans1 += (manhattan(xa, ya, xb+1, yb)+manhattan(xc, yb, xc, yc))
    # 自分が荷物の左側にいて、目的地も荷物の左側にある場合
    if xa-xb<0 and xc-xb<0:
        # 荷物の右側に移動して、荷物のx座標を目的地のx座標に揃える
        ans1 += (manhattan(xa, ya, xb+1, yb)+manhattan(xc, yb, xc, yc))
        # y座標が最初から同じ場合は+2
        if ya==yb:
            ans1 += 2
    # 自分が荷物の左側にいて、目的地が荷物の右側にある場合
    if xa-xb<0 and xc-xb>0:
        # 荷物の左側に移動して、荷物のx座標を目的地のx座標に揃える
        ans1 += (manhattan(xa, ya, xb-1, yb)+manhattan(xc, yb, xc, yc))
else:
    # 自分が荷物と目的地の間にいる場合
    if (yb-ya)*(yc-ya)<0:
        ans1 += manhattan(xa, ya, xb, yb)-1+manhattan(xb, yb, xc, yc)+4
    else:
        ans1 += manhattan(xa, ya, xb, yb)-1+manhattan(xb, yb, xc, yc)


# 荷物と目的地のy座標を揃える
# この時点でx座標は揃っている
# if yc-yb!=0:
#    ans1 += manhattan(xb, yb, xc, yc)

# y座標を先に揃える場合
ans2 = 0
# 荷物と目的地のy座標を揃える
if yc-yb!=0:
    # 自分が荷物の上側にいて、目的地も荷物の上側にある場合
    if ya-yb>0 and yc-yb>0:
        # 荷物の下側に移動して、荷物のy座標を目的地のy座標に揃える
        ans2 += (manhattan(xa, ya, xb, yb-1)+manhattan(xb, yc, xc, yc))
        # x座標が最初から同じ場合は+2
        if xa==xb:
            ans2 += 2
    # 自分が荷物の上側にいて、目的地が荷物の下側にある場合
    if ya-yb>0 and yc-yb<0:
        # 荷物の上側に移動して、荷物のy座標を目的地のy座標に揃える
        ans2 += (manhattan(xa, ya, xb, yb+1)+manhattan(xb, yc, xc, yc))
    # 自分が荷物の下側にいて、目的地も荷物の下側にある場合
    if ya-yb<0 and yc-yb<0:
        # 荷物の上側に移動して、荷物のy座標を目的地のy座標に揃える
        ans2 += (manhattan(xa, ya, xb, yb+1)+manhattan(xb, yc, xc, yc))
        # x座標が最初から同じ場合は+2
        if xa==xb:
            ans2 += 2
    # 自分が荷物の下側にいて、目的地が荷物の上側にある場合
    if ya-yb<0 and yc-yb>0:
        # 荷物の下側に移動して、荷物のy座標を目的地のy座標に揃える
        ans2 += (manhattan(xa, ya, xb, yb-1)+manhattan(xb, yc, xc, yc))
else:
    # 自分が荷物と目的地の間にいる場合
    if (xb-xa)*(xc-xa)<0:
        ans2 += manhattan(xa, ya, xb, yb)-1+manhattan(xb, yc, xc, yc)+4
    else:
        ans2 += manhattan(xa, ya, xb, yb)-1+manhattan(xb, yc, xc, yc)

# 荷物と目的地のx座標を揃える
# この時点でy座標は揃っている
# if xc-xb!=0:
#    ans2 += manhattan(xb, yb, xc, yc)

print(ans1)
print(ans2)