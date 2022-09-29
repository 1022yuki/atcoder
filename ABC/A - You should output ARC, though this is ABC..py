R, C = map(int, input().split())

A = []
a1 = list(map(int, input().split()))
A.append(a1)
a2 = list(map(int, input().split()))
A.append(a2)

print(A[R-1][C-1])