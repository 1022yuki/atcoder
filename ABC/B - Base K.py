K = int(input())

A, B = map(str, input().split())

def Base(K, A):
  sum10 = 0
  for i in range(0, len(A)):
    sum10 += (K**i) * int(A[len(A)-i-1])
  return sum10

a = Base(K, A)
b = Base(K, B)

print(a*b)