def solve(s):
	result,num = [], 0
	for x in s:
		if x not in ['a', 'e', 'i', 'o', 'u']:
			num += ord(x) - 96
		else:
			result.append(num)
			num = 0
	return max(result)




print(solve('mischtschenkoana'))


# 大佬鼠

import re

def solve(s):
	return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))