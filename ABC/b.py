from collections import Counter

S = input()
SS = list(S)

mycounter = Counter(SS)

# print(mycounter.most_common(1)[0][1])

# print(.isupper())

if mycounter.most_common(1)[0][1] == 1 and S.isupper() == False and S.islower() == False:
  print('Yes')
else:
  print('No')