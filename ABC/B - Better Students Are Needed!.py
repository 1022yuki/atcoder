N, X, Y, Z = map(int, input().split())

M = list(map(int, input().split()))

E = list(map(int, input().split()))

acc = []

s = []

for i in range(N):
  s.append([M[i], E[i], M[i]+E[i], N-(i+1)])

# print(s)

sorted_s1 = sorted(s, key=lambda x:(x[0], x[3]))

# print(sorted_s1)

for i in range(X):
  acc.append(N-(sorted_s1[-1][3]))
  del sorted_s1[-1]

sorted_s2 = sorted(sorted_s1, key=lambda x:(x[1], x[3]))
for i in range(Y):
  acc.append(N-(sorted_s2[-1][3]))
  del sorted_s2[-1]

sorted_s3 = sorted(sorted_s2, key=lambda x:(x[2], x[3]))
for i in range(Z):
  acc.append(N-(sorted_s3[-1][3]))
  del sorted_s3[-1]

acc.sort()

# print(acc)

for x in acc:
  print(x)