def who_is_winner(pieces_position_list):
	print(pieces_position_list)
	info = [[], [], [], [], [], [], []]
	for i in range(len(pieces_position_list)):
		a_list = pieces_position_list[i].split('_')
		k,v = ord(a_list[0]) -65,a_list[1]
		info[k].append(v)
	for i in range(4):
		for j in range(7):
			try:
				if info[j][i] == info[j + 1][i + 1] == info[j + 2][i + 2] == info[j + 3][i + 3]:
					return info[j][i]
			except IndexError:
				continue
		for j in range(7):
			try:
				if info[j][i] == info[j - 1][i + 1] == info[j - 2][i + 2] == info[j - 3][i + 3]:
					return info[j][i]
			except IndexError:
				continue
	return 'Draw'


a = who_is_winner(['C_Yellow', 'B_Red', 'B_Yellow', 'E_Red', 'D_Yellow', 'G_Red', 'B_Yellow', 'G_Red', 'E_Yellow', 'A_Red', 'G_Yellow', 'C_Red', 'A_Yellow', 'A_Red', 'D_Yellow', 'B_Red', 'G_Yellow', 'A_Red', 'F_Yellow', 'B_Red', 'D_Yellow', 'A_Red', 'F_Yellow', 'F_Red', 'B_Yellow', 'F_Red', 'F_Yellow', 'G_Red', 'A_Yellow', 'F_Red', 'C_Yellow', 'C_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'D_Red', 'E_Yellow', 'D_Red', 'E_Yellow', 'C_Red', 'E_Yellow', 'E_Red'])
print(a)