N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count1 = 0
count2 = 0

for i in range(0, N):
  if A[i] == B[i]:
    count1 += 1

for i in range(0, N):
  for j in range(0, N):
    if i != j:
      if A[i] == B[j]:
        count2 += 1

print(count1)
print(count2)