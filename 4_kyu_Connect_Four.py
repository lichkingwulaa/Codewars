def check(array):
	# 行
	for i in range(7):
		for j in range(3):
			if array[i][j] == array[i][j + 1] == array[i][j + 2] == array[i][j + 3] != '0':
				return array[i][j]

	# 列
	for j in range(6):
		for i in range(4):
			if array[i][j] == array[i + 1][j] == array[i + 2][j] == array[i + 3][j] != '0':
				return array[i][j]

	# 左斜
	for i in range(4):
		for j in range(3):
			if array[i][j] == array[i + 1][j + 1] == array[i + 2][j + 2] == array[i + 3][j + 3] != '0':
				return array[i][j]

	# 右斜
	for j in range(3, 6):
		for i in range(4):
			if array[i][j] == array[i + 1][j - 1] == array[i + 2][j - 2] == array[i + 3][j - 3] != '0':
				return array[i][j]

def who_is_winner(array):
	print(array)
	# 将数据填入数组
	res = [['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],
	       ['0','0','0','0','0','0'],]
	for x in array:
		alpha, color = x.split('_')
		row = ord(alpha) - 65
		column = res[row].index('0')
		res[row][column] = color[0]
		result = check(res)
		if result == 'Y':
			return 'Yellow'
		if result == 'R':
			return 'Red'
	return 'Draw'


winner = who_is_winner(['F_Red', 'B_Yellow', 'D_Red', 'F_Yellow',
                        'G_Red', 'F_Yellow', 'F_Red', 'B_Yellow',
                        'E_Red', 'E_Yellow', 'B_Red', 'C_Yellow',
                        'C_Red', 'A_Yellow', 'F_Red', 'E_Yellow',
                        'B_Red', 'D_Yellow', 'F_Red'])
print(winner)