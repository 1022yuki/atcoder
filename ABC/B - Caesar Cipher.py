S = list(input())
T = input()

print(ord(S[0]))

newS = []

for i in range(1, 27):
  for j in range(1, 3):
    asc = ord(S[j])
    if asc + i <= 122:
      asc += i
    else:
      asc += (i-26)
    char = chr(asc)
    newS.append(char)
  
  newS = "".join(newS)
  print(newS)

  if newS == T:
    print('Yes')