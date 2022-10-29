N = int(input())

mod_3 = N//3
mod_5 = N//5
mod_7= N//7
mod_15 = N//15
mod_21 = N//21
mod_35 = N//35
mod_105 = N//105

ans = mod_3+mod_5+mod_7-mod_15-mod_21-mod_35+mod_105
print(ans)