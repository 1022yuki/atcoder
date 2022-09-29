from collections import defaultdict

N = int(input())

person = []
for i in range(N):
  x, y = map(int, input().split())
  person.append((x, y))

S = input()

# print(person)

dict = defaultdict(int)

for i in range(N):
  x, y = person[i]
  dire = S[i]
  if dict[y] == 0:
    if dire == 'L':
      dict[y] = (x, 10**10)
    else:
      dict[y] = (-10**10, x)
  else:
    now_L, now_R = dict[y]
    if dire == 'L' and x > now_L:
      dict[y] = (x, now_R)
    if dire == 'R' and x < now_R:
      dict[y] = (now_L, x)

# print(dict)

for x in dict.values():
  if x[0] > x[1]:
    print('Yes')
    exit()

print('No')