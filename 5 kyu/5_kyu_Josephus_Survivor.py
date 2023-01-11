def josephus_survivor(n,k):
	items = list(range(n))
	res = []
	i = k - 1
	while items:
		i = i % len(items)
		res.append(items.pop(i))
		i += (k - 1)
	return res[-1] + 1


print(josephus_survivor(7,3),4)
print(josephus_survivor(11,19),10)
print(josephus_survivor(1,300),1)
print(josephus_survivor(14,2),13)
print(josephus_survivor(100,1),100)