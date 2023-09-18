A, B = map(int, input().split())

c = str(B/A)

# if len(c)<=5:
#   d = float(c)
# else:
#   if int(c[5])>=5:
#     d = float(c[:5])+0.001
#   else:
#     d = float(c[:5])
d = round((B/A), 3)

sup = 5-len(str(d))
print(str(d)+'0'*sup)