N = int(input())
D = list(map(int, input().split()))

sensor1 = list(map(int, input().split()))
sensor2 = list(map(int, input().split()))

num1 = sensor1[2]
num2 = sensor2[2]
NumList = []

for i in range(N):
  NumList = NumListTmp
  NumListTmp = []
  for n1, n2 in NumList:
    lg = D[i]
    if lg % sensor1[0] == 0:
      numSensor1Max = lg // sensor1[0]
    else:
      numSensor1Max = lg // sensor1[0] + 1
    for n in range(numSensor1Max+1):
      numSensor1 = n
      remDist = lg - numSensor1*sensor1[0]
      if remDist % sensor2[0] == 0:
        numSensor2 = remDist // sensor2[0]
      else:
        numSensor2 = remDist // sensor2[0] + 1
      if numSensor1<=num1 and numSensor2<=num2:
        num1 -= numSensor1
        num2 -= numSensor2
    NumListTmp.append([num1, num2])