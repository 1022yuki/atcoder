import math
A, B = map(int, input().split())

n = ((A/(2*B))**(2/3))-1
# print(n)

n1 = math.floor(n)
n2 = math.floor(n)+1

# print(n1)
# print(n2)

def f(n):
  if n < 0:
    ans = 10**20
  else:
    ans = A/((n+1)**0.5)+n*B
  return ans

ans1 = f(n1)
ans2 = f(n2)

print(min(ans1, ans2))