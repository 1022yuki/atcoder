N, K = map(int, input().split())

# S = []
# for i in range(0, N):
#   s = list(input())
#   S.append(s)

S = []
for i in range(0, N):
  s = input()
  S.append(s)

# print(N)
# print(K)

# print(S)

# for i in range(0, len(S)):
#   print()
#   mycounter = Counter(S[i])
#   for word in mycounter.most_common():
#       print(word)

STR = ''
for i in range(0, N):
  STR += S[i]

# print(STR)

alp = []
alp.append(STR.count('a'))
alp.append(STR.count('b'))
alp.append(STR.count('c'))
alp.append(STR.count('d'))
alp.append(STR.count('e'))
alp.append(STR.count('f'))
alp.append(STR.count('g'))
alp.append(STR.count('h'))
alp.append(STR.count('i'))
alp.append(STR.count('j'))
alp.append(STR.count('k'))
alp.append(STR.count('l'))
alp.append(STR.count('m'))
alp.append(STR.count('n'))
alp.append(STR.count('o'))
alp.append(STR.count('p'))
alp.append(STR.count('q'))
alp.append(STR.count('r'))
alp.append(STR.count('s'))
alp.append(STR.count('t'))
alp.append(STR.count('u'))
alp.append(STR.count('v'))
alp.append(STR.count('w'))
alp.append(STR.count('x'))
alp.append(STR.count('y'))
alp.append(STR.count('z'))

count = 0

for i in alp:
  if i >= K:
    count += 1

print(count)