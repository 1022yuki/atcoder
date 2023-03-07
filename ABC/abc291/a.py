S = input()
len = len(S)

# print(ord("A"))

for i in range(len):
  if ord(S[i]) >= ord('A') and ord(S[i]) <= ord('Z'):
    print(i+1)