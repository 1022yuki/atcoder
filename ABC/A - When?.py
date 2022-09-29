K = int(input())

if 0 <= K < 10:
  print("21:0" + str(K))
elif K < 60:
  print("21:" + str(K))
elif K < 70:
  print("22:0" + str(K-60))
else:
  print("22:" + str(K-60))