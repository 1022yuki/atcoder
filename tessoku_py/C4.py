N = int(input())

root = int(N**0.5)
Y = set()
for i in range(1 ,root+1):
  if N%i==0:
    Y.add(i)
    Y.add(N//i)

li_Y = list(Y)
li_Y.sort()

for i in range(len(li_Y)):
  print(li_Y[i])