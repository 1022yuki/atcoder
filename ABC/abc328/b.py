N = int(input())
D = list(map(int, input().split()))

cnt = 0
for m in range(1, N+1):
  month = str(m)
  for d in range(1, D[m-1]+1):
    day = str(d)
    # ゾロ目判定
    if len(month)==1:
      if len(day)==1:
        if month==day:
          cnt += 1
          # print(month, day)
      if len(day)==2:
        if month==day[1] and day[0]==day[1]:
          cnt += 1
          # print(month, day)
    if len(month)==2:
      if len(day)==1:
        if month[1]==day and month[0]==month[1]:
          cnt += 1
          # print(month, day)
      if len(day)==2:
        if month[1]==day[1] and month[0]==day[0] and month[0]==month[1]:
          cnt += 1
          # print(month, day)
    

print(cnt)