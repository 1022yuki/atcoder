N, K, X = map(int, input().split())
A = list(map(int, input().split()))

full = 0
rem = []
for i in range(N):
  full += A[i]//X
  rem.append(A[i]%X)

full = min(full, K)
rem.sort(reverse=True)

# print(K-full)
# print(rem)
part = 0
rep = min(K-full, len(rem))
for i in range(rep):
  part += rem[i]

all = sum(A)-full*X-part

print(all)