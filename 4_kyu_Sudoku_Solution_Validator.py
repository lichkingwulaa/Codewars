"""
https://www.codewars.com/kata/sudoku-solution-validator/python
"""
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

value = validSolution(
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]])
print(value)



# 汪小佬
import numpy as np
def validSolution1(board):
	board = np.array(board)
	for i in range(9):
		if len(set(board[i])) != 9 or len(set(board.T[i])) != 9:
			return False
	for i in range(0, 7, 3):
		for j in range(0, 7, 3):
			if board[i:i + 3, j:j + 3].sum() != 45:
				return False
	return True


# 大佬鼠
def validSolution2(board):
	blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
	return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)