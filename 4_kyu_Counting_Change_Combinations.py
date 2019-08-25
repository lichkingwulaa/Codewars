def count_change(money, coins):
	if money < 0 or len(coins) == 0:
		return 0
	elif money == 0:
		return 1
	else:
		return count_change(money - coins[-1], coins) + count_change(money, coins[:-1])


a = 419
b = [2, 5, 10, 20, 50]
c = count_change(a,b)
print(c)


# 大佬鼠的迷惑解法
def count_change(money, coins):
	ways = [1] + [0] * (money + 1)
	for coin in coins:
		for i in range(coin, money + 1):
			ways[i] += ways[i - coin]
	return ways[money]