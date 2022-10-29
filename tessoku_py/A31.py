N = int(input())

mod_3 = N // 3
mod_5 = N // 5
mod_15 = N // 15

ans = mod_3+mod_5-mod_15
print(ans)