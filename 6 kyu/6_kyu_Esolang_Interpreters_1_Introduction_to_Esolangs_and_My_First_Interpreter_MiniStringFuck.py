import re
def my_first_interpreter(code):
	code = re.sub(r'[^+.]', '', code)
	num = [len(x) for x in re.findall(r'\++', code)]
	res = ''
	for i in range(len(num)):
		value = sum(num[:i + 1])
		while value >= 256:
			value -= 256
		res += chr(value)
	return res

solution = my_first_interpreter
print(my_first_interpreter('+++++sdfs++++sdf++++sdklfjsdklfdjmvncxmnxmiuroewurwio+++++++++++++2423423++234+23++234+23++342+2++24++234++++++++++++++???++++++%+++++$#$#++++++++.+++++ssdf+++++++++++++++S+SDFSFSFWWET+BCV+BC+VBN+V+X+++.+++++++.WER.+++.++++++++++++++++++WERW+ERWE++++++++++++XCV+XC++++++++++++++++CXV+XC+XCV++++++++++++++++++++++++XCVXCXCVSTTYJFGDF++++++++++++++++s+dfs+sdf++sdsd+f++SDFS+DFS+FdfsdRTETRCBVCsdfsdf++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'))   # 'Hello, World!'
print(my_first_interpreter('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'))   # 'Hello, World!'
print(my_first_interpreter('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.')) # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



# 大佬鼠(平平淡淡才是真)
def my_first_interpreter(code):
	memory, output = 0, ""
	for command in code:
		if command == "+":
			memory += 1
		elif command == ".":
			output += chr(memory % 256)
	
	return output