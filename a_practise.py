import time



def count_change(money, coins):
	ways = [1] + [0] * (money + 1)
	for coin in coins:
		for i in range(coin, money + 1):
			ways[i] += ways[i - coin]
	return ways[money]


a = 419
b = [2, 5, 10, 20, 50]

# a = 300
# b = [5, 10, 20, 50, 100, 200, 500]

start = time.time()
c = count_change(a,b)
print(c)
end = time.time()
print('time:'+ str(end - start))

