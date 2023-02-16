N, Q = map(int, input().split())
S = input()

A = []
B = []
C = []
D = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

mod = 998244353

kisu = [100]
for i in range(N):
  kisu.append((kisu[-1]*100)%mod)

# print(kisu)

# hash値の前計算
# Sの1文字目からi文字目までのhash値(基数100)
H = [0]

for i in range(N):
  H.append((H[-1]*100+ord(S[i])-ord("a")+1)%mod)

# print(H)

for i in range(Q):
  a, b, c, d = A[i], B[i], C[i], D[i]
  hash_ab = (H[b]-H[a-1]*kisu[b-a])%mod
  hash_cd = (H[d]-H[c-1]*kisu[d-c])%mod
  # print(hash_ab)
  # print(hash_cd)
  if hash_ab == hash_cd:
    print('Yes')
  else:
    print('No')