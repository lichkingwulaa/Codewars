def delete_zero_and_comp(array):
	array = [x for x in array if x != 0]
	if len(set(array)) != len(array):
		return False

def validSolution_isok(board):
	for i in range(9):
		# row
		delete_zero_and_comp(board[i])
		# column
		column = [board[j][i] for j in range(9)]
		delete_zero_and_comp(column)

	num = []
	for x in range(0,3,6):  # 每列3个格子
		for y in range(0,3,6):  # 每行3个格子
			for i in range(x,x+3):  # 每个格子
				for j in range(y,y+3):
					num.append(board[i][j])
			delete_zero_and_comp(num)

	return True



# 测试用
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

a = set(range(10)) | set(range(5)) | set(range(15))
print(a)