import bisect

N = int(input())
A = list(map(int, input().split()))

X = sorted(list(set(A)))

# print(X)

B = [None] * N

for i in range(N):
  B[i] = bisect.bisect_right(X, A[i])

print(*B)