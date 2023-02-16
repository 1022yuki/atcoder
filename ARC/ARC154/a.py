N = int(input())
A = list(input())
B = list(input())

mod = 998244353

for i in range(N):
  if A[i] > B[i]:
    c = A[i]
    A[i] = B[i]
    B[i] = c

i_a = "".join(A)
i_b = "".join(B)

m_a = int(i_a)%mod
m_b = int(i_b)%mod

print((m_a*m_b)%mod)