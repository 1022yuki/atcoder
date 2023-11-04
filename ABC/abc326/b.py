N = int(input())

while True:
  # print(N)
  if int(str(N)[0])*int(str(N)[1])==int(str(N)[2]):
    print(N)
    exit()
  else:
    N+=1