def tickets(people):
	money = {25: 0, 50: 0, 100: 0}
	for x in people:
		money[x] += 1
		if x == 50:
			money[25] -= 1
		if x == 100:
			if money[50] > 0:
				money[50] -= 1
				money[25] -= 1
			else:
				money[25] -= 3
		if money[25] < 0 or money[50] < 0 or money[100] < 0:
			return 'NO'
	return 'YES'

print(tickets([25, 50, 50]))