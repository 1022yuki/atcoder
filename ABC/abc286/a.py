N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

# print(A[:P-1])
# print(A[P-1:Q])
# print(A[Q:R-1])
# print(A[R-1:S])
# print(A[S:])

print(*(A[:P-1]+A[R-1:S]+A[Q:R-1]+A[P-1:Q]+A[S:]))