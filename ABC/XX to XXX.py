S = list(input())
T = list(input())

Sl = []
Tl = []

Sl.append([S[0]])
Tl.append([T[0]])

countS = [0]
countT = [0]

for i in range(1, len(S)):
  if S[i] == S[i-1]:
    if len(Sl[-1])<2:
      Sl[-1].append(S[i])
    else:
      countS[-1] += 1
  else:
    Sl.append([S[i]])
    countS.append(0)

for i in range(1, len(T)):
  if T[i] == T[i-1]:
    if len(Tl[-1])<2:
      Tl[-1].append(T[i])
    else:
      # print(countT[-1])
      countT[-1] += 1
  else:
    Tl.append([T[i]])
    countT.append(0)


# print(Sl)
# print(Tl)

# print(countS)
# print(countT)

state = False
if len(countT) == len(countS):
  state = True
  for i in range(len(countT)):
    if countS[i] > countT[i]:
      state = False

if Sl == Tl and state:
  print('Yes')
else:
  print('No')