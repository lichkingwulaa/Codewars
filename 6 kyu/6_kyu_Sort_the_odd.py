def sort_array(array):
	curr = [i for i in range(len(array)) if array[i] % 2]
	odd = sorted(array[i] for i in range(len(array)) if array[i] % 2)
	for i, j in enumerate(curr):
		array[j] = odd[i]
	return array



print(sort_array([5, 3, 2, 8, 1, 4]))


# 大佬鼠
def sort_array(arr):
	odds = sorted((x for x in arr if x%2 != 0), reverse=True)
	return [x if x%2==0 else odds.pop() for x in arr]