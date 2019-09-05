def isprime(n):
	for i in range(3, max(n, int(str(n)[::-1])) // 3 + 1, 2):
		if n % i == 0:
			return False
	return True




def reversible_prime():

	pass


print(reversible_prime(), 2)
print(reversible_prime(), 3)
print(reversible_prime(), 13)
print(reversible_prime(), 73)
print(reversible_prime(), 167)
print(reversible_prime(), 1669)
