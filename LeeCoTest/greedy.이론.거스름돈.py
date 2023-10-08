money = 1260
coins = [500, 100, 50, 10]
cnt = 0
for coin in coins:
    share, remainders = money // coin, money % coin
    
    cnt += share
    money = remainders

print(cnt)
