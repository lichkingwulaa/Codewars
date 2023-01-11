def find_nb(m):
	n = int((2 * m ** 0.5) ** 0.5)
	return n if sum(x ** 3 for x in range(n + 1)) == m else -1
	# return n if n * (n + 1) / 2 == m * 0.5 else -1

print(find_nb(1025292944081385001))
print(find_nb(4183059834009)) #2022
print(find_nb(24723578342962))#-1



def find_nb(m):
	n = 1
	volume = 0
	while volume < m:
		volume += n**3
		if volume == m:
			return n
		n += 1
	return -1
