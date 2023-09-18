from collections import defaultdict

S = input()

dic = defaultdict(list)

for i in range(8):
  dic[S[i]].append(i)

# print(dic)
# print(dic['B'][1]-dic['B'][0])

if (dic['B'][1]-dic['B'][0])%2==1:
  # print('aaaaaaaa')
  if dic['R'][1]-dic['K'][0]>0 and dic['R'][0]-dic['K'][0]<0:
    print('Yes')
    exit()

print('No')