def interpreter(code, iterations, width, height):
	code = ''.join(x for x in code if x in 'nesw*[]')
	res = [['0' for x in range(width)] for y in range(height)]  # 初始化
	left = [i for i, x in enumerate(code) if x == '[']
	right = [i for i, x in enumerate(code) if x == ']'][::-1]
	num, count, i, j = 0, 0, 0, 0
	while iterations > 0 and count < len(code) and num < iterations:
		i = (i + height) % height
		j = (j + width) % width
		if code[count] == 'n':
			i -= 1
		elif code[count] == 'e':
			j += 1
		elif code[count] == 's':
			i += 1
		elif code[count] == 'w':
			j -= 1
		elif code[count] == '*':
			res[i][j] = str((int(res[i][j]) + 1) % 2)
		elif code[count] == '[' and res[i][j] == '0':
			count = right[left.index(count)]
		elif code[count] == ']' and res[i][j] == '1':
			count = left[right.index(count)]
		count += 1
		num += 1
	return '\r\n'.join(''.join(x) for x in res)


print(interpreter('*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*', 7, 6, 9))


# 大佬鼠
def interpreter(code, iterations, width, height):
	code = "".join(c for c in code if c in "[news]*")
	canvas = [[0] * width for _ in range(height)]
	row = col = step = count = loop = 0
	
	while step < len(code) and count < iterations:
		command = code[step]
		
		if loop:
			if command == "[":
				loop += 1
			elif command == "]":
				loop -= 1
		
		elif command == "n":
			row = (row - 1) % height
		elif command == "s":
			row = (row + 1) % height
		elif command == "w":
			col = (col - 1) % width
		elif command == "e":
			col = (col + 1) % width
		elif command == "*":
			canvas[row][col] ^= 1
		elif command == "[" and canvas[row][col] == 0:
			loop += 1
		elif command == "]" and canvas[row][col] != 0:
			loop -= 1
		
		step += 1 if not loop else loop // abs(loop)
		count += 1 if not loop else 0
	
	return "\r\n".join("".join(map(str, row)) for row in canvas)