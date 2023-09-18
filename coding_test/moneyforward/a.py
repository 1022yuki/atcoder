deposit_amount, years, interest_rate = map(float, input().split())
deposit_amount = int(deposit_amount)
years = int(years)

if years<3:
    # 単利計算
    interest = int(deposit_amount*interest_rate*0.01*years)
    received_amount = deposit_amount+interest
else:
    # 複利計算
    received_amount = deposit_amount
    for n in range(2*years):
        if n%2==0:
            # 最初の半年
            interest = int(received_amount*interest_rate*0.01*(182/365))
            received_amount = received_amount+interest
        else:
            # 後半の半年
            interest = int(received_amount*interest_rate*0.01*(183/365))
            received_amount = received_amount+interest

print(received_amount)