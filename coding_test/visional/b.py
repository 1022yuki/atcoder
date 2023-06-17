n = list(input())

for i in range(len(n)):
    n[i] = int(n[i])

n1 = n.copy()
if 0 in n1:
  n1 = [num for num in n1 if num != 0]
# print(n)
# print(n1)

n1.sort()
pre = n1[0]
ans = []
ans.append(str(pre))

n.remove(pre)
n.sort()

for i in range(len(n)):
   ans.append(str(n[i]))
   
print(''.join(ans))