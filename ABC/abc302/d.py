N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

ans = -1

for i in range(N):
    gift_1 = A[i]
    right = gift_1+D
    ng = M
    ok = -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if B[mid]<=right:
            ok = mid
        else:
            ng = mid
    # print(B[ok])
    gift_2 = B[ok]
    if abs(gift_2-gift_1)<=D:
        ans = max(ans, gift_2+gift_1)

print(ans)