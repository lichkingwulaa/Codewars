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
from random import randint
print(randint(0,1))