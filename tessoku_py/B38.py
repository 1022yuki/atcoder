N = int(input())
S = list(input())

H1 = [1]*N
H2 = [1]*N
H = [10**5]*N

for i in range(N-1):
  if S[i]=="A":
    H1[i+1] = H1[i]+1

for i in range(N-2, -1, -1):
  if S[i]=="B":
    H2[i] = H2[i+1]+1

# print(H1)
# print(H2)

for i in range(N):
  H[i] = max(H1[i], H2[i])

# print(H)
print(sum(H))