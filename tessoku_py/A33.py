N = int(input())
A = list(map(int, input().split()))

XOR_sum = A[0]
for i in range(1, N):
  XOR_sum = XOR_sum ^ A[i]

if XOR_sum != 0:
  print('First')
else:
  print('Second')