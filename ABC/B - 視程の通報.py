m = int(input())

if m < 100:
  print('00')
elif m <= 5000:
  if m//100 < 10:
    print('0'+str(m//100))
  else:
    print(str(m//100))
elif 6000 <= m <= 30000:
  print(str(m//1000+50))
elif 35000 <= m <= 70000:
  print (str((m//1000-30)//5+80))
elif m > 70000:
  print('89')