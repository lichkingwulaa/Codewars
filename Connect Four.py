def who_is_winner(pieces_position_list):
	print(pieces_position_list)
	info = [[],[],[],[],[],[],[]]
	for m in range(7):
		for n in range(6):
			info[m].append('0')
	for i in range(len(pieces_position_list)):
		a_list = pieces_position_list[i].split('_')
		num = ord(a_list[0]) -65
		info[num].append(a_list[1])
		for x in range(7):
			for y in (3, 4, 5):
				try:
					if x <= 3:
						if info[x][y] == info[x + 1][y - 1] == info[x + 2][y - 2] == info[x + 3][y - 3] != '0':
							return info[x][y]
					if x >= 3:
						if info[x][y] == info[x - 1][y - 1] == info[x - 2][y - 2] == info[x - 3][y - 3] != '0':
							return info[x][y]
				except IndexError:
					continue
		
		for x in range(7):
			for y in range(6):
				try:
					if x <= 3:
						if info[x][y] == info[x+1][y] == info[x+2][y] == info[x+3][y] != '0':
							return info[x][y]
					if x >= 3:
						if info[x][y] == info[x][y+1] == info[x][y+2] == info[x][y+3] != '0':
							return info[x][y]
				except IndexError:
					continue
	return 'Draw'
a = who_is_winner(['A_Yellow', 'B_Red', 'B_Yellow', 'C_Red',
                   'G_Yellow', 'C_Red', 'C_Yellow', 'D_Red',
                   'G_Yellow', 'D_Red', 'G_Yellow', 'D_Red',
                   'F_Yellow', 'E_Red', 'D_Yellow'])
print(a)

print(range(1,7))