N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

# cnt_A[i]: ソートされた配列Aの中に、B[i]よりも小さな値がいくつ入っているかを保持
# cnt_C[i]: ソートされた配列Cの中に、B[i]よりも大きな値がいくつ入っているかを保持
# 求める答えは全てのiについて、cnt_A[i]*cnt_C[i] を足し合わせたもの

cnt_A = []
cnt_C = []

# cnt_A, cnt_C の中身を埋める
for b in B:
  ng = -1
  ok = N
  while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if A[mid] >= b:
      ok = mid
    else:
      ng = mid
  cnt_A.append(ok)

for b in B:
  ng = -1
  ok = N
  while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if C[mid] > b:
      ok = mid
    else:
      ng = mid
  cnt_C.append(N-ok)

# print(cnt_A)
# print(cnt_C)

cnt = 0
for i in range(N):
  cnt += cnt_A[i]*cnt_C[i]

print(cnt)