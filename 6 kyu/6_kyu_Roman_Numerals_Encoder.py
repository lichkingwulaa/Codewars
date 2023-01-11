def solution(n):
	# TODO convert int to roman string
	res = ['',] * len(str(n))
	d = ['M', 'C', 'X' ,'I']
	for i in range(1, len(str(n)) + 1):
		res[-i] = int(str(n)[-i]) * d[-i]
	res = ''.join(res)
	res = res.replace('I' * 9, 'IX').replace('X' * 9, 'XC').replace('C' * 9, 'CM')
	res = res.replace('I' * 5, 'V').replace('X' * 5, 'L').replace('C' * 5, 'D')
	res = res.replace('I' * 4, 'IV').replace('X' * 4, 'XL').replace('C' * 4, 'CD')
	return res

print(solution(1989))

# 大佬鼠
vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,  90,   50,  40,   10,   9,   5,    4,   1))
def solution1(n):
	if n == 0: return ""
	return next(c + solution(n-v) for c,v in vals if v <= n)

def solution2(n):
	roman_numerals = {1000:'M',
                      900: 'CM',    90: 'XC',   9: 'IX',
                      500: 'D',     50: 'L',    5: 'V',
                      400: 'CD',    40: 'XL',   4: 'IV',
                      100: 'C',     10: 'X',    1: 'I'    }
	roman_string = ''
	for key in sorted(roman_numerals.keys(),reverse=True):
		while n >= key:
			roman_string += roman_numerals[key]
			n -= key
	return roman_string