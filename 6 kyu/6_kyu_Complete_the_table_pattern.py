def pattern(rows, columns, s):
	s += ' ' * rows * columns
	res = '+---' * columns + '+\n|'
	for i in range(rows * columns):
		if i % columns == 0 and i:
			res += '\n' + '+---' * columns + '+\n|'
		res += ' ' + s[i] + ' |'
	res += '\n' + '+---' * columns + '+'
	return res



pattern(4, 4, "Hello World!")

# 正确结果
result = """\
+---+---+---+---+
| H | e | l | l |
+---+---+---+---+
| o |   | W | o |
+---+---+---+---+
| r | l | d | ! |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""