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

a = validSolution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                   [4, 9, 8, 2, 6, 1, 3, 7, 5],
                   [7, 5, 6, 3, 8, 4, 2, 1, 9],
                   [6, 4, 3, 1, 5, 8, 7, 9, 2],
                   [5, 2, 1, 7, 9, 3, 8, 4, 6],
                   [9, 8, 7, 4, 2, 6, 5, 3, 1],
                   [2, 1, 4, 9, 3, 5, 6, 8, 7],
                   [3, 6, 5, 8, 1, 7, 9, 2, 4],
                   [8, 7, 9, 6, 4, 2, 1, 3, 5]])
print(a)


# 行row
# 列column