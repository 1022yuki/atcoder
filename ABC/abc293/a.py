S = list(input())

l = len(S)//2
for i in range(l):
  one = 2*i
  two = 2*i+1
  c = S[one]
  S[one] = S[two]
  S[two] = c

print("".join(S))