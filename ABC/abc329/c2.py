N = int(input())
S = list(input())

aSet = set()

i = 0
st = S[0]
while True:
  aSet.add(st)
  if i==N:
    break
  if i!=N-1 and S[i]==S[i+1]:
    st = ''.join([st, S[i]])
    i+=1
  else:
    st = S[i]
    i+=1

# print(aSet)
print(len(aSet))