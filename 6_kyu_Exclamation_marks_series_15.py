"""
https://www.codewars.com/kata/exclamation-marks-series-number-15-replace-the-pair-of-exclamation-marks-and-question-marks-to-spaces/python
"""
import re
def replace(s):
	s = re.findall(r'!+|\?+', s)
	for i, x in enumerate(s):
		if '!' in x and '?' * len(x) in s:
			s[i] = s[s.index('?' * len(x))] = ' ' * len(x)
		elif '?' in x and '!' * len(x) in s:
			s[i] = s[s.index('!' * len(x))] =' ' * len(x)
	return ''.join(s)

print(replace("?!!?!!?!!?!!!??!!!??!!!??!!!??!!!??"), "\n?  ?  ?  ?!!!  !!!  !!!  !!!??!!!??")
print(replace("!?!!??!!!?"), "\n      !!!?")