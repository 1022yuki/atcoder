s = int(input())

# print(s//10)

strs = str(s//10)

len = len(strs)

if len == 1:
  print('000'+strs)
elif len == 2:
  print('00'+strs)
elif len == 3:
  print('0'+strs)