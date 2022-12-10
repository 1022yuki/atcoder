N, Q = map(int, input().split())
S = input()

L = []
R = []
for i in range(Q):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

mod = 998244353

T = []
for i in range(N):
  num = ord(S[i])-ord('a')+1
  T.append(num)

pow100 = [1]
for i in range(N):
  pow100.append((pow100[-1]*100)%mod)

# ハッシュ値の前計算
H1 = [0]
H2 = [0]
for i in range(N):
  H1.append((H1[-1]*100+T[i])%mod)
  H2.append((H2[-1]*100+T[N-i-1])%mod)

# print(H1)
# print(H2)

# 前からのハッシュ
def hash1(l, r):
  val = (H1[r]-(H1[l-1]*pow100[r-l+1]))%mod
  return val
# 後ろからのハッシュ
def hash2(l, r):
  val = (H2[r]-(H2[l-1]*pow100[r-l+1]))%mod
  return val

# print(hash1(4, 6))
# print(hash2(4, 6))

for i in range(Q):
  l = L[i]
  r = R[i]
  # print(hash1(l, r))
  # print(hash2(N-r+1, N-l+1))
  if hash1(l, r) == hash2(N-r+1, N-l+1):
    print('Yes')
  else:
    print('No')