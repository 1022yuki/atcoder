X = list(input())

X.sort()

if X[0] == '0':
    for i in range(1, len(X)):
        if X[i] != '0':
            X[0], X[i] = X[i], X[0]
            break

print("".join(X))