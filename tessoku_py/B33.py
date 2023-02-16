N, H, W = map(int, input().split())
A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a-1)
  B.append(b-1)

all_mnt = A+B

xor = 0
for i in range(2*N):
  xor ^= all_mnt[i]

# print(xor)

if xor == 0:
  print("Second")
else:
  print("First")