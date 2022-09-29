A = list(map(int, input().split()))

def botan(i):
  return A[i]

a1 = botan(0)
a2 = botan(a1)
a3 = botan(a2)

print(a3)