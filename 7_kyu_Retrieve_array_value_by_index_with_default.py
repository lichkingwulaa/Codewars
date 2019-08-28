"""
https://www.codewars.com/kata/retrieve-array-value-by-index-with-default/train/python
"""
def solution(items, index, default_value):
	try:
		return items[index]
	except IndexError:
		return default_value


rng = list(range(1, 4))
print(solution(rng, -5, 'a'))


def solution(items, index, default_value):
	return items[index] if -len(items) <= index <len(items) else default_value

