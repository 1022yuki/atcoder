N = int(input())

st_N = str(N)
ln_N = len(st_N)

ans = 0

# 何桁目か
for i in range(ln_N):
  # print(ans)
  dig_num = int(st_N[i])
  kisu = 10**(ln_N-i-1)
  # print(i, kisu)

  if i==0:
    # 先頭の桁
    for n in range(1, 10):
      if n < dig_num:
        ans += n * kisu

      if n == dig_num:
        ans += n * ((N%kisu)+1)
    continue
  
  if i==ln_N-1:
    # 最後の桁
    for n in range(1, 10):
      if n <= dig_num:
        ans += n*((N//(kisu*10))+1)
      else:
        ans += n*(N//(kisu*10))
      # print(ans)
    continue
  
  # 先頭、最後以外の桁 
  for n in range(1, 10):
    div = N//(kisu*10)
    div_2 = N%(kisu)
    if n < dig_num:
      ans += n * kisu * (div+1)
    
    if n == dig_num:
      ans += n * (kisu*div+(div_2+1))

    if n > dig_num:
      ans += n * kisu * (div)

print(ans)