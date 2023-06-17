N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = []
R = []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


okiteru = []
neteru = []
for i in range(N-1):
    if i%2==0:
        okiteru.append([A[i], A[i+1]])
    else:
        neteru.append([A[i], A[i+1]])

# print(okiteru)
# print(neteru)

# 累積和
Sum = [0]
for i in range(len(neteru)):
    Sum.append(Sum[-1] + neteru[i][1] - neteru[i][0])

print(Sum)
# print()
# print()

import bisect
asn = []
for i in range(Q):
    l = L[i]
    r = R[i]
    l_ind = bisect.bisect_right(A, l)
    r_ind = bisect.bisect_right(A, r)
    # print(l_ind, r_ind)
    if r_ind%2==1:
        # rが起床中の時間だった時
        r_sum = Sum[((r_ind+1)//2)-1]
    else:
        # rが睡眠中の時間だった時
        r_sum = Sum[((r_ind+1)//2)-1]+(r-A[r_ind-1])
    if l_ind%2==1:
        # lが起床中の時間だった時
        l_sum = Sum[((l_ind+1)//2)-1]
    else:
        # lが睡眠中の時間だった時
        l_sum = Sum[((l_ind+1)//2)-1]+(l-A[l_ind-1])
    print(r_sum-l_sum)