N = int(input())
S = input()

import re

spl = S.split('"')

# print(spl)

for i in range(len(spl)):
  if i%2==0:
    st = spl[i]
    spl[i] = re.sub(",", ".", st)

# print(spl)

ans = '"'.join(spl)
print(ans)