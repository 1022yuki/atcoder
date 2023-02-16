D = int(input())
X = int(input())
A = []
for i in range(D-1):
  a = int(input())
  A.append(a)
Q = int(input())
queries = []
for i in range(Q):
  s, t = map(int, input().split())
  queries.append([s, t])

sum = [0, X]
for i in range(D-1):
  sum.append(sum[-1]+A[i])

# print(sum)

for i in range(Q):
  s, t = queries[i]
  if sum[s] > sum[t]:
    print(s)
  elif sum[s] == sum[t]:
    print("Same")
  else:
    print(t)