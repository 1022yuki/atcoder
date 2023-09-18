from collections import defaultdict
import re

S = input()

dic = defaultdict(int)
mul = 1

# li = re.sub(r'([a-z])', r'1(\1)', S)
# print(li)

re.search(r'([0-9]+)[a-z]', S)

num_li = re.split(r'[a-z\(\)]+', S)
num_li = [i for i in num_li if i!='']
print(num_li)

st_s = re.sub(r'[0-9]', '', S)
print(st_s)

mul_li_af = []

for st in st_s:
  # print(mul)
  # print(num_li)
  # print(mul_li_af)
  # print()
  if st=='(':
    weight = int(num_li.pop(0))
    mul *= weight
    mul_li_af.append(weight)
  elif st==')':
    mul //= mul_li_af.pop()
  else:
    dic[st]+=mul

print(dic)