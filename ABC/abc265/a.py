X, Y, N = map(int, input().split())

am_3 = N // 3
am_1 = N % 3

if Y/3 < X:
  ans = Y * am_3 + X * am_1
else:
  ans = X * N

print(ans)