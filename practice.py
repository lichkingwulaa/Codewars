import time
a = time.time()

from itertools import count

def num_primorial(n):
	prime = [2,]
	for x in range(3, 200000, 2):
		for i in range(3, x // 2 + 1, 2):
			if x % i == 0: break
		else:
			prime.append(x)
	final_prime = [x for x in prime if int(str(x)[::-1]) in prime]
	print(final_prime)
	print(len(final_prime))

num_primorial(0)


b = time.time()
print(b-a,'s')

