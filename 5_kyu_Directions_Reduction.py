"""
https://www.codewars.com/kata/directions-reduction/solutions/python
"""
def dirReduc(arr):
	i = 0
	while True:
		if i + 1 - len(arr) >= 0:
			return arr
		if sorted([arr[i],arr[i+1]]) in [['NORTH', 'SOUTH'] , ['EAST', 'WEST']]:
			del arr[i]
			del arr[i]
			i = 0
		else:
			i += 1

a = dirReduc(['EAST', 'NORTH', 'SOUTH', 'WEST', 'WEST'])
print(a)



# 大佬鼠的迷惑方法
def dirReduc1(arr):
	dir1 = " ".join(arr)
	dir2 = dir1.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
	dir3 = dir2.split()
	return dirReduc(dir3) if len(dir3) < len(arr) else dir3


def dirReduc2(arr):
	while True:
		dir1 = " ".join(arr)
		dir2 = dir1.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
		dir3 = dir2.split()
		if len(dir3) >= len(arr):
			break
		arr = dir3[:]
	return dir3