N = int(input())
A = list(map(int, input().split()))

diff = []

A.sort()

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# factorization(24) 

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

s1 = set(A)
# print(s1)

# print(len(s1))

# if len(s1) == 1:
#   print(1)
#   exit()
if N == 2 and A[0] == A[-1]:
  print(1)
  exit()

A = list(s1)
A.sort()
min_1 = A[0]
min_2 = A[-1]
diff = min_2-min_1

# print(factorization(diff))

mod = []
for x, y in factorization(diff):
  mod.append(x)

# print(mod)

for MOD in mod:
  if MOD >= 2:
    B = A.copy()
    first = B[0] % MOD
    state2 = True
    for i in range(N):
      if B[i] % MOD != first:
        state2 = False
        continue
    if state2:
      print(1)
      exit()

print(2)