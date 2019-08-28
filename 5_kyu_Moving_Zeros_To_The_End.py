"""
https://www.codewars.com/kata/moving-zeros-to-the-end/train/python
"""
def move_zeros(array):
	i = count = 0
	while count < len(array):
		if type(array[i]) != bool and array[i] == 0:
			array.append(array.pop(i))
		else:
			i += 1
		count += 1
	return array

a = move_zeros([9,False, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0.0, 0, 0.0, 0, 0, 0] )
print(a)

# 大佬鼠的迷惑方法
def move_zeros1(array):
	return sorted(array,key=lambda x:x==0 and type(x) != bool)

def move_zeros2(arr):
	l = [i for i in arr if isinstance(i, bool) or i!=0]
	return l+[0]*(len(arr)-len(l))