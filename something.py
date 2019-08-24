def histogram(rolls):
	cur = [ ['#'] * x + [str(x)] + [' '] * (max(rolls) - x) if x else [' '] * (max(rolls)  + 1)for x in rolls ]
	res = []
	for j in range(max(rolls) + 1):
		a = []
		for i in range(len(rolls)):
			a.append(cur[i][j] + ' ')
		res.append(a)
	b = ''
	for x in res[::-1]:
		b += ''.join(x).rstrip() + '\n'
	b += '-' * (len(rolls) * 2 - 1) + '\n'
	b += ' '.join(str(x) for x in (range(1, len(rolls) + 1))) + '\n'
	return b
	
	
	
roll = [7,3,10,1,0,5]
print(histogram(roll))

# "    10\n"+
# "    #\n"+
# "    #\n"+
# "7   #\n"+
# "#   #\n"+
# "#   #     5\n"+
# "#   #     #\n"+
# "# 3 #     #\n"+
# "# # #     #\n"+
# "# # # 1   #\n"+
# "# # # #   #\n"+
# "-----------\n"+
# "1 2 3 4 5 6\n"