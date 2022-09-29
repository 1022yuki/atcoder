S = input()

have = []
prob = []

for i in range(10):
  s = S[i]
  if s == 'o':
    have.append(i)
  if s == '?':
    prob.append(i)

# print(have)
# print(prob)

num = have + prob
num.sort()
len = len(num)

cnt = 0

for i in range(len):
  for j in range(len):
    for k in range(len):
      for l in range(len):
        # numに含まれる数字について4桁の数字を作る
        ans = []
        ans.append(num[i])
        ans.append(num[j])
        ans.append(num[k])
        ans.append(num[l])
        # print(ans)
        state = True
        for x in have:
          ok = False
          for y in ans:
            if x == y:
              ok = True
          if ok:
            continue
          else:
            state = False
        if state:
          cnt += 1

print(cnt)