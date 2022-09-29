import math

a, b, d = map(int, input().split())

sita = d*math.pi/180

a2 = a*math.cos(sita)-b*math.sin(sita)
b2 = a*math.sin(sita)+b*math.cos(sita)

print(str(a2) + " " + str(b2))