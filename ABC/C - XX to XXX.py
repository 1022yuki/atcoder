S = list(input())
T = list(input())


for i in range(0, len(S)-2):
  if S[i] == S[i+1] == S[i+2]:
    S[i] = ''

for i in range(0, len(T)-2):
  if T[i] == T[i+1] == T[i+2]:
    T[i] = ''

print(S)
print(T)

S2 = ''
T2 = ''

sss = []
for i in range(len(S)):
  if S[i] != '':
    sss.append(S[i])

ttt = []
for i in range(len(T)):
  if T[i] != '':
    ttt.append(T[i])

if S2 == T2:
  print('Yes')
else:
  print('No')