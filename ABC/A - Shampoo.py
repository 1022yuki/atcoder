V, A, B, C = map(int, input().split())

sham = V

while(sham >= 0):
  sham -= A
  if sham < 0:
    print('F')
    break
  sham -= B
  if sham < 0:
    print('M')
    break
  sham -= C
  if sham < 0:
    print('T')
    break