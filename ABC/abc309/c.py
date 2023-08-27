from collections import defaultdict

N, K = map(int, input().split())

dic = defaultdict(int)
nomu = 0
A = []
# B = []
for i in range(N):
    a, b = map(int, input().split())
    dic[a] += b
    nomu += b
    A.append(a)
    # B.append(b)

# print(dic)
A = list(set(A))
A.sort()
# print(nomu)
if nomu <= K:
    print(1)
    exit()

for i in range(N):
    nomu -= dic[A[i]]
    # print(nomu)
    if nomu <= K:
        print(A[i]+1)
        exit()