N = int(input())
X = list(map(int, input().split()))

X.sort()

# print(X)

po = X[N:4*N]

# print(po)

print(sum(po)/(3*N))