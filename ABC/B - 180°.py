S = list(input())

def rotate(s):
  if s == '0':
    return '0'
  elif s == '1':
    return '1'
  elif s == '6':
    return '9'
  elif s == '8':
    return '8'
  elif s == '9':
    return '6'

S.reverse()

# print(S)

for i in range(len(S)):
  S[i] = rotate(S[i])

# print(S)

str_ans = ''
for x in S:
  str_ans += x

print(str_ans)