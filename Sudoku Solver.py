def validSolution(board):
	for i in range(9):
		# row
		if len(set(board[i])) != 9:
			return False
		# column
		column = [board[j][i] for j in range(9)]
		if len(set(column)) != 9:
			return False
	num = []
	for x in range(0,3,6):  # 每列3个格子
		for y in range(0,3,6):  # 每行3个格子
			for i in range(x,x+3):  # 每个格子
				for j in range(y,y+3):
					num.append(board[i][j])
			if len(set(num)) != 9:
				return False
	return True

def num(row, collumn):
	"""返回可填入的数字列表"""
	return [x for x in range(1,10) if x not in row and x not in collumn]

def sudoku(puzzle):
	"""return the solved puzzle as a 2d array of 9 x 9"""
	row,column,old_puzzle = [],[],puzzle
	for i in range(9):
		row.append([puzzle[i][j] for j in range(9)])
		column.append([puzzle[j][i] for j in range(9)])
	while True:
		puzzle = old_puzzle
		for i in range(9):
			for j in range(9):
				board = num(row[i], column[j])
				if len(board) == 0:
					break
				if len(board) != 0 and puzzle[i][j] == 0:
					puzzle[i][j] = num(row[i],column[j]).pop(-1)
					row[i][j] = puzzle[i][j]
					column[j][i] = puzzle[i][j]
			else:
				continue
			break
		if validSolution(puzzle):
			return puzzle
	


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))