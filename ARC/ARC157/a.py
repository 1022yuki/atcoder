N, A, B, C, D = map(int, input().split())

if B==0 and C==0:
  if A==0 or D==0:
    print("Yes")
    exit()
  else:
    print("No")
    exit()

if abs(B-C)<=1:
  print("Yes")
else:
  print("No")