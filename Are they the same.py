def comp(array1, array2):
	if not array1 or None:
		return False
	i = 0
	while True:
		if array1[i]**2 in array2:
			array2.remove(array1[i] ** 2)
			array1.remove(array1[i])
			if len(array1) == 0:
				if len(array2) == 0:
					return True
				else:
					return False
			i = 0
		else:
			return False

a1 = [121, 144, 19, 161,  19, 144, 19, 11 ]
a2 = [11*11, 121*121, 144*144,19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1,a2))