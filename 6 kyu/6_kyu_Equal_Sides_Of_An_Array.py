def find_even_index(arr):
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i + 1:]):
			return i
	return -1

print(find_even_index([20,10,-80,10,10,15,35]))


# 大佬鼠
def find_even_index1(arr):
	r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
	return r[0] if r else -1


find_even_index2 = lambda arr: next((i for i, __ in enumerate(arr) if sum(arr[:i]) == sum(arr[i+1:])), -1)