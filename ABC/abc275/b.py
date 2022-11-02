A, B, C, D, E, F = map(int, input().split())

mod = 998244353
ab = (A*B)%mod
Abc = (ab*C) % mod

de = (D*E)%mod
Def = (de*F)%mod

ans = (Abc-Def)%mod
if ans<0:
  ans += mod
print(ans)