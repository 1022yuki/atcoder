N =int(input())

S = []
for i in range(0, N):
  s = input()
  S.append(s)

# print(S)

mayans = [0]*10
# ターゲットNo.それぞれについて最小値を調べる
for i in range(0, 10):
  # print(i)
  tar = i
  # 純粋にかかる時間
  time = []
  # かかる時間が同じだともう1周しないといけないことを考慮した時間
  time_comp = []
  # 各リールについて
  for j in range(0, N):
    # 文字列を見て、ターゲットNoと同じだったらかかる秒数(indexNoと同じ)をtime[j]=kとする
    for k in range(0, 10):

      # その時点でtimeの中を見て、kと同じものがあったらその数だけ＋10して格納する

      if int(S[j][k]) == tar:
        count = 0
        for l in range(0, len(time)):
          if time[l] == k:
            count += 1
        time.append(k)
        time_comp.append(k+10*count)


    # print(time)
    
  mayans[i] = max(time_comp)

ans = min(mayans)
print(ans)