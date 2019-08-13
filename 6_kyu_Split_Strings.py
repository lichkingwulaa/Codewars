def solution(s):
	return [ s[i:i + 2] for i in range(0, len(s) - 1, 2)] + ([s[-1] + '_'] if len(s) % 2 == 1 else [])


print(solution(''))

# 大佬鼠
import re
def solution1(s):
	return re.findall(".{2}", s + "_")

def solution2(s):
	return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution3(s):
	return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]