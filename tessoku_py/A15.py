import bisect

N = int(input())
A = list(map(int, input().split()))

X = sorted(list(set(A)))

# print(X)

B = []

for i in range(N):
  B.append(bisect.bisect_left(X, A[i])+1)

print(*B)