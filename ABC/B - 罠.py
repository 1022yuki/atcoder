W = input()

# def eliminate(x):
#   if x=='a' or x=='i' or x=='u' or x=='e' or x=='o':
#     return True
#   else:
#     return False

ans = W.replace('a', '').replace('i', '').replace('u', '').replace('e', '').replace('o', '')

print(ans)

