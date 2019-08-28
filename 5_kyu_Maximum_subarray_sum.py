"""
https://www.codewars.com/kata/maximum-subarray-sum/train/python
"""
def maxSequence(arr):
	num = [0]
	for i in range(len(arr)):
		sum = 0
		for j in range(i,len(arr)):
			sum += arr[j]
			num.append(sum)
	return max(num)
	
a = maxSequence([-5])
print(a)


# 大佬鼠的迷惑方法
def maxSequence1(arr):
	max,num = 0,0
	for x in arr:
		num += x
		if num < 0:
			num = 0
		if num > max:
			max = num
	return max