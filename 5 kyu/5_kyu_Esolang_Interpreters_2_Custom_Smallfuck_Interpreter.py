def interpreter(code, tape):
	left = [i for i, x in enumerate(code) if x == '[']
	right = [i for i, x in enumerate(code) if x == ']'][::-1]
	tape = list(tape)
	i, count = 0, 0
	while not (count >= len(tape) or count < 0 or i >= len(code)):
		if code[i] == '*':
			tape[count] = str((int(tape[count]) + 1) % 2)
		elif code[i] == '<':
			count -= 1
		elif code[i] == '>':
			count += 1
		elif code[i] == '[' and tape[count] == '0':
			i = right[left.index(i)]
		elif code[i] == ']' and tape[count] == '1':
			i = left[right.index(i)]
		i += 1
	return ''.join(tape)


print(interpreter('*[>*]',
                  '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))


# 大佬鼠
def interpreter(code, tape):
	tape = list(map(int, tape))
	ptr = step = loop = 0
	
	while 0 <= ptr < len(tape) and step < len(code):
		command = code[step]
		
		if loop:
			if command == "[":
				loop += 1
			elif command == "]":
				loop -= 1
		
		elif command == ">":
			ptr += 1
		elif command == "<":
			ptr -= 1
		elif command == "*":
			tape[ptr] ^= 1
		elif command == "[" and tape[ptr] == 0:
			loop += 1
		elif command == "]" and tape[ptr] == 1:
			loop -= 1
		
		step += 1 if not loop else loop // abs(loop)
	
	return "".join(map(str, tape))