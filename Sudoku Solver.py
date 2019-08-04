"""return the solved puzzle as a 2d array of 9 x 9"""
def nine(array):
	num = []
	nine_block = []
	for x in (0, 3, 6):  # 每列3个格子
		for y in (0, 3, 6):  # 每行3个格子
			for i in range(x, x + 3):  # 每个格子
				for j in range(y, y + 3):
					num.append(array[i][j])
			nine_block.append(num)
			num = []
	return nine_block

def row_and_column(array):
	row = []
	column = []
	for i in range(9):
		# row
		row.append(array[i])
		# column
		column.append([array[j][i] for j in range(9)])
	return row,column

def num_set(array,nine_block):
	pick_set = {}
	row,column = row_and_column(array)
	for i in range(9):
		for j in range(9):
			if array[i][j] == 0:
				pick_set[str(i) + str(j)] = set(range(10)) - \
					(set(nine_block[3 * (i // 3) + j // 3]) | set(row[i]) | set(column[j]))
	return pick_set

def sudoku(puzzle):
	step = [] # 记录填入的列值对，即在何处填入何值
	while True:
		pick_set = num_set(puzzle,nine(puzzle))
		if len(pick_set) == 0:
			break
		pick_sort = sorted(pick_set.items(), key=lambda x: len(x[1])) # 按字典内的值的长度升序排序
		item_min = pick_sort[0] # 获取第一队列值对
		key = item_min[0] # 列
		value = list(item_min[1]) # 值
		step.append((key, value)) # 记录填入的列值对，即在何处填入何值
		if len(value) == 0:
			step.pop()  # 删除本次填数的记录
			for i in range(len(step)):
				last_one = step.pop()
				last_key = last_one[0]
				last_value = last_one[1]
				if len(last_value) == 1:
					puzzle[int(last_key[0]), int(last_key[1])] = 0
				else:
					puzzle[int(last_key[0]), int(last_key[1])] = last_value[1]
					step.append((last_key, last_value[1:]))
					break
		else:
			puzzle[int(key[0])][int(key[1])] = value[0]  # 填入数值
	return puzzle




date = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(date))