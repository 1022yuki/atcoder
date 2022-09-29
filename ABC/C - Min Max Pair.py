import math
N = int(input())
a = list(map(int, input().split()))

def comb(n):
  fact = math.factorial(n - 2)
  return ((fact*(n-1)*n) // (fact * 2))

  # return math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))

li = [0] + a

# print(li)

com = 0
only = 0
for i in range(1, N+1):
  if li[i] == i:
    com += 1 
  
  elif li[li[i]] == i:
    only += 1

# print(com)
# print(math.comb(com, 2))
# print(only)

nC2 = 0
if com >= 2:
  nC2 = comb(com)

print(nC2+only//2)