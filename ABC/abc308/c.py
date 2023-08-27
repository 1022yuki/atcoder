from decimal import Decimal,getcontext
getcontext().prec = 50
# import fractions

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def reduce(p, q):
    common = gcd(p, q)
    return (p // common, q // common)

N = int(input())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


li = []
for i in range(N):
    a = A[i]
    b = B[i]
    suc = Decimal(a) / Decimal(a+b)
    # c, d = reduce(a, a+b)
    # suc = c/d
    # print(c, d)
    li.append([-suc, i+1])

li.sort()

for i in range(N):
    print(li[i][1], end=' ')
print()