S = input()
T = input()

from collections import defaultdict

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for s in S:
  dic1[s] += 1

for t in T:
  dic2[t] += 1

print(dic1)
print(dic2)

set = 'atcoder'

for s in set:
  # print(s)
  num1 = dic1[s]
  num2 = dic2[s]
  print(num1, num2)

# while True:

import requests

while True:
  # print(to_next)
  response = requests.get("https://challenge-server.code-check.io/api/kidnapper/deliver"+"?token="+args[1]+"?to="+to_next)
  # print("レスポンス2")
  if response.json()["put_the_bag"]!=None:
      print(response.json()["put_the_bag"])
      exit()
  to_next = response.json()["goto"]