N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

max_a = max(A)
grundy = [0]*(max_a+1)
for i in range(1, max_a+1):
  # 移動先のgrundy数を記録
  transit = {0: False, 1: False, 2: False}
  if i>=X:
    transit[grundy[i-X]] = True
  if i>=Y:
    transit[grundy[i-Y]] = True
  if not transit[0]:
    grundy[i] = 0
  elif not transit[1]:
    grundy[i] = 1
  else:
    grundy[i] = 2

xor = 0
for i in range(N):
  xor ^= grundy[A[i]]

# print(grundy)

if xor == 0:
  print("Second")
else:
  print("First")