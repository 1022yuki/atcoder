def GCD(A, B):
  while(A>=1 and B>=1):
    if A >= B:
      A = A % B
    else:
      B = B % A

  if A != 0:
    return A
  else:
    return B

A, B = map(int, input().split())

gcd = GCD(A, B)
lcm = A*B // gcd
print(lcm)