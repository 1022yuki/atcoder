import math

N, A, B = map(int, input().split())


sum_all = (N * (N+1)) // 2

# sum_allから(Aの倍数orBの倍数)を引く

Anum = N // A
Bnum = N // B

# 最小公倍数 AB=LG を利用
lcm = A*B//math.gcd(A, B)
ABnum = N // lcm

maxA = A*Anum
maxB = B*Bnum
maxAB = lcm*ABnum

if A==1 or B==1:
  ans = 0
elif N == 1:
  ans = 1
else:
  subA = Anum*(A+maxA) // 2
  subB = Bnum*(B+maxB) // 2
  subAB = ABnum*(lcm+maxAB) // 2

  ans = sum_all - subA - subB + subAB

print(ans)