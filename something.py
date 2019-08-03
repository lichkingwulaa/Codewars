def move_zeros(array):
	return sorted(array,key=lambda x:x==0 and type(x) != bool)


a = move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
print(a)

