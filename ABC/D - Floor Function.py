A, B, N = map(int, input().split())

if N <= B-1:
  cul = int(A*N/B) - A*int(N/B)
else:
  cul = int(A*(B-1)/B) - A*int((B-1)/B)

print(cul)