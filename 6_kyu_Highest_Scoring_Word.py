"""
https://www.codewars.com/kata/highest-scoring-word/train/python
"""
def high(x):
	d = { 'a': 1,  'b': 2,  'c': 3,  'd': 4,  'e': 5,  'f': 6,  'g': 7,
	      'h': 8,  'i': 9,  'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
	      'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
	      'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26  }
	string = x.split(' ')
	num = [ sum(d[x] for x in s ) for s in string ]
	return string[num.index(max(num))]


print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')