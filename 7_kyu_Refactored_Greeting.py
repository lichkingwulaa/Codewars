"""
https://www.codewars.com/kata/refactored-greeting/solutions/python
"""
class Person:
	def __init__(self, name):
		self.name = name

	def greet(self, your_name):
		return "Hello %s, my name is %s" % (your_name, self.name)


jill = Person('Jill')
print(jill.greet("Mark"))
print(jill.name)