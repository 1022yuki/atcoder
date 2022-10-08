Q = int(input())

# nが素数の時True
def is_prime(n):
  LIM = int(n**0.5)
  for i in range(2, LIM+1):
    if n % i == 0:
      return False
  return True

queries = []
for i in range(Q):
  queries.append(int(input()))


for num in queries:
  # print(num)
  if is_prime(num):
    print('Yes')
  else:
    print('No')