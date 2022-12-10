N = int(input())
A = list(map(int, input().split()))

def dev2(n):
  num2 = 0
  while n % 2 == 0:
    n //= 2
    num2 += 1
  return n, num2

def dev3(n):
  num3 = 0
  while n % 3 == 0:
    n //= 3
    num3 += 1
  return n, num3

# print(dev2(40))
deved = []

num_3_all = []
num_2_all = []

for i in range(N):
  dev_3, num_3 = dev3(A[i])
  dev_2 , num_2= dev2(dev_3)
  num_3_all.append(num_3)
  num_2_all.append(num_2)
  deved.append(dev_2)

# print(A)
# print(deved)

fir = deved[0]
for i in range(1, N):
  if deved[i] != fir:
    print(-1)
    exit()

# print()
# print(num_2_all)
# print(num_3_all)


ans = sum(num_2_all)+sum(num_3_all)
# print(ans)
ans -= min(num_2_all) *N
ans -= min(num_3_all) *N
print(ans)