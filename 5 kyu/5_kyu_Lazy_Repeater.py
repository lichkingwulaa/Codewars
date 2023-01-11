def make_looper(string):
	x = -1
	def f():
		nonlocal x
		x += 1
		return string[x % len(string)]
	return f

a = make_looper('abc')
a()
a()
a()
a()
a()
a()
a()



# 大佬鼠
from itertools import cycle
def make_looper1(s):
	g = cycle(s)
	return lambda: next(g)

def make_looper2(string):
	def generator():
		while True:
			for char in string:
				yield char
	return generator().next


make_looper3=lambda s,c=__import__("itertools").cycle: c(s).__next__