def check(first_array):
	array = first_array
	for i in range(7):
		array[i] += ['0','0','0','0','0','0']

	# 行
	for i in range(4):
		for j in range(6):
			if array[i][j] == array[i + 1][j] == array[i + 2][j] == array[i + 3][j] != '0':
				return array[i][j]

	# 列
	for i in range(7):
		for j in range(3):
			if array[i][j] == array[i][j + 1] == array[i][j + 2] == array[i][j + 3] != '0':
				return array[i][j]

	# 右斜
	for i in range(4):
		for j in range(3):
			if array[i][j] == array[i + 1][j + 1] == array[i + 2][j + 2] == array[i + 3][j + 3] != '0':
				return array[i][j]

	# 左斜
	for i in range(3, 7):
		for j in range(3):
			if array[i][j] == array[i - 1][j + 1] == array[i - 2][j + 2] == array[i - 3][j + 3] != '0':
				return array[i][j]

	return 'Draw'

def who_is_winner(array):
	print(array)
	# 将数据填入数组
	final_array = [[],[],[],[],[],[],[]]
	for i in range(len(array)):
		a_coclr = array[i].split('_')
		num = ord(a_coclr[0]) - 65
		final_array[num].append(a_coclr[1])

		result = check(final_array[:])
		if result in ['Yellow','Red']:
			return result
	
	return 'Draw'




a = who_is_winner(
	['C_Yellow', 'B_Red', 'B_Yellow', 'E_Red', 'D_Yellow', 'G_Red', 'B_Yellow', 'G_Red', 'E_Yellow', 'A_Red',
	 'G_Yellow', 'C_Red', 'A_Yellow', 'A_Red', 'D_Yellow', 'B_Red', 'G_Yellow', 'A_Red', 'F_Yellow', 'B_Red',
	 'D_Yellow', 'A_Red', 'F_Yellow', 'F_Red', 'B_Yellow', 'F_Red', 'F_Yellow', 'G_Red', 'A_Yellow', 'F_Red',
	 'C_Yellow', 'C_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'D_Red', 'E_Yellow', 'D_Red', 'E_Yellow', 'C_Red',
	 'E_Yellow', 'E_Red']
                  )
print(a)