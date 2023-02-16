S = list(input())
T = list(input())

# print(S)
# print(T)

lt = len(T)
ls = len(S)
# for i in range(lt+1):
  # print(i)
  # print(lt+i-1)
  # print(S[:i])
  # print(S[ls-(lt-i):])
  # s2 = S[:i]+S[ls-(lt-i):]
  # print(s2)
  # print(T)
  # print()


dig = set()
# for i in range(lt+1):
#   s = set()
#   dig.append(s)

fir = S[ls-lt:]
for i in range(lt):
  if fir[i] != T[i]:
    if fir[i] != "?" and T[i] != "?":
      dig.add(i)

if len(dig) == 0:
  print('Yes')
else:
  print('No')

for i in range(lt):
  nsi = S[i]
  if nsi != T[i] and nsi != "?" and T[i] != "?":
    dig.add(i)
  else:
    dig.discard(i)
  
  # print(dig)
  if len(dig) == 0:
    print('Yes')
  else:
    print('No')