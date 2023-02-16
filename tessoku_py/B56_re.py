N, Q = map(int, input().split())
S = list(input())
L = []
R = []
for i in range(Q):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

mod = 998244353

# hash値の前計算
# Sの1文字目からi文字目までのhash値(基数100)
H = [0]
for i in range(N):
  H.append((H[-1]*100+ord(S[i])-ord("a")+1)%mod)

# reverseしたhash値の前計算
S_rev = list(reversed(S))
H_rev = [0]
for i in range(N):
  H_rev.append((H_rev[-1]*100+ord(S_rev[i])-ord("a")+1)%mod)

# print(H)
# print(H_rev)

kisu = [100]
for i in range(N-1):
  kisu.append((kisu[-1]*100)%mod)

# print(kisu)

def hash_val(l, r, hash):
  value = (hash[r]-hash[l-1]*kisu[r-l])%mod
  return value

# print(hash_val(2, 5, H))
# print(hash_val(7, 10, H_rev))

for i in range(Q):
  l, r = L[i], R[i]
  if hash_val(l, r, H) == hash_val(N-r+1, N-l+1, H_rev):
    print('Yes')
  else:
    print('No')