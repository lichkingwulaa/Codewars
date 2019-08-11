dic = { '0': 'black', '1': 'brown', '2': 'red',    '3': 'orange',  '4': 'yellow',
		'5': 'green', '6': 'blue',  '7': 'violet', '8': 'gray',    '9': 'white',    }

def encode_resistor_colors(bands):
	num = bands.split(' ')[0]
	num = int(float(num[:-1]) * 10 ** 3) if 'k' in num else int(float(num[:-1]) * 10 ** 6) if 'M' in num else int(num)
	return dic[str(num)[0]] + ' ' + dic[str(num)[1]] + ' ' + dic[str(len(str(num)) - 2)] + ' gold'

print(encode_resistor_colors('4.7k ohms'))


# 大佬鼠的迷惑方法1
def encode_resistor_colors1(bands):
	num = str(int(eval(bands.split(' ')[0].replace('k', '*1000').replace('M', '*1000000'))))
	return "{} {} {} gold".format(dic[num[0]], dic[num[1]], dic[str(len(num[2:]))])


# 大佬鼠的迷惑方法2(x, y, *z)
def encode_resistor_colors2(bands):
	x, y, *z = str(int(eval(bands.split(' ')[0].replace('k', '*1000').replace('M', '*1000000'))))
	return "{} {} {} gold".format(dic[x], dic[y], dic[str(len(z))])