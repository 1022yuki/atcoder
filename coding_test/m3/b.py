A = list(map(int, input().split(',')))

ans = []
for i in range(len(A)):
    if i%2 == 1:
        # 偶数番目は残す
        ans.append(A[i])
    elif i!=0 and A[i]==A[i-1]:
        # 取り除く1つ前の値と同じ値だった場合残す
        ans.append(A[i])

print(*ans, sep=',')