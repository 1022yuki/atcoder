import re

S = input()
T = input()

new = re.sub(T,'',S)
# print(new)

if len(new) < len(S):
  print('Yes')
else:
  print('No')