N, M = map(int, input().split())

T = []
X = []
not_use_kankiri = []
use_kankiri = []
kankiri = []

for i in range(N):
    t, x = map(int, input().split())
    T.append(t)
    X.append(x)
    if t==0:
        not_use_kankiri.append(x)
    if t==1:
        use_kankiri.append(x)
    if t==2:
        kankiri.append(x)

not_use_kankiri.sort(reverse=True)
use_kankiri.sort(reverse=True)
kankiri.sort(reverse=True)

len_kankiri = len(kankiri)

for i in range(len_kankiri+1):
    