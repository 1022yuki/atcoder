n = input()
digit = len(n)
l = int(n)

sum = 0

def g(x):
  sum = 0
  for i in range(10**(x-1), 10**x):
    sum += i-(10**(x-1)-1)
  return sum

def h(x):
  sum = 0
  for i in range(10**(x-1), l+1):
    sum += i-(10**(x-1)-1)
  return sum

for i in range(1, digit):
  sum += g(i)

sum += h(digit)

rem = sum % 998244353

print(rem)