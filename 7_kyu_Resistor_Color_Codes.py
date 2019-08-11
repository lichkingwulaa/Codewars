dic = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
       'green': '5', 'blue': '6', 'violet': '7', 'gray': '8', 'white': '9',
       'gold': '5%', 'silver': '10%', 'color': '20%'}   # 将20%也加入字典

def the_num(bands):
	result = ''
	for i in range(len(bands) - 2):         # 十的乘方以外的数字
		result += dic[bands[i]]
	result += '0' * int(dic[bands[-2]])     # 添加十的乘方
	kM = ['', 'k', 'M']                         # 换算为‘k’‘M’
	if int(result) >= 1000000:  i = 2
	elif int(result) >= 1000:     i = 1
	else: i = 0
	num = int(result) / 10 ** (3 * i)
	if num == int(num):  num = int(num)
	result = str(num) + kM[i]
	return result

def decode_resistor_colors(bands):
	bands = bands.split(' ')
	if bands[-1] not in ['gold', 'silver']:
		bands.append('color')
	result = the_num(bands)
	result += ' ohms, '
	result += dic[bands[-1]]
	return result


print(decode_resistor_colors("yellow violet black"))