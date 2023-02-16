N = int(input())
A = list(map(int, input().split()))

e_or = A[0]
for i in range(1, len(A)):
  e_or ^= A[i]

if e_or == 0:
  print("Second")
else:
  print("First")