A, B, K = map(int, input().split())

if K<=A:
  t = A-K
  a = B
elif K <= A+B:
  t = 0
  a = B-(K-A)
else:
  t = 0
  a = 0

print(t, a)