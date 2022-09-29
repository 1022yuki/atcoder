n, k = list(map(int, input().split()))

sum = 0

for i in range(n):
  for j in range(k):
    num = int(str(i+1)+"0"+str(j+1))
    sum += num

print(sum)