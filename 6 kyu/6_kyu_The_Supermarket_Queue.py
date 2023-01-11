def queue_time(customers, n):
	if not customers:
		return 0
	elif len(customers) <= n:
		return max(customers)
	else:
		res =[ [customers[i]] for i in range(n) ]
		for i in range(n, len(customers)):
			res[sorted((sum(x), j) for j, x in enumerate(res))[0][1]].append(customers[i])
		return max(sum(x) for x in res)



print(queue_time([], 1))



def queue_time(customers, n):
	res = [0] * n
	for i in customers:
		res[res.index(min(res))] += i
	return max(res)