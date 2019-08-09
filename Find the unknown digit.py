def solve_runes(runes):
	print(runes)
	num_pick = [i for i in range(10) if str(i) not in runes]
	runes = runes.replace('--','+').replace('=', '==')

	for i in num_pick:
		runes_re = runes.replace('?', str(i))
		if eval(runes_re):
			if runes_re == str(eval(runes_re)):
				return i
	return -1

r = solve_runes('??*1=??')
print(r)

a = '22*1==22'
if eval(a):
	print('bingo')
print((eval(a)))