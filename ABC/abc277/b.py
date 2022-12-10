N = int(input())

li = []
for i in range(N):
  inp = input()
  li.append(inp)

set_li = set(li)

if len(li) != len(set_li):
  print('No')
  exit()

for i in range(N):
  if li[i][0] != 'H' and  li[i][0] != 'D' and li[i][0] != 'C' and li[i][0] != 'S':
    print('No')
    exit()

for i in range(N):
  if li[i][1] != 'A' and  li[i][1] != '2' and li[i][1] != '3' and li[i][1] != '4' and li[i][1] != '5' and  li[i][1] != '6' and li[i][1] != '7' and li[i][1] != '8' and li[i][1] != '9' and  li[i][1] != 'T' and li[i][1] != 'J' and li[i][1] != 'Q' and li[i][1] != 'K':
    print('No')
    exit()

print('Yes')