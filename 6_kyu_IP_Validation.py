import re
def is_valid_IP(strng):
	return True if re.fullmatch(r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}', strng)\
		else False


print(is_valid_IP('1.2.3.4.5'))

"""
0-9         \d
10-99       [1-9]\d
100-199     1\d{2}
200-249     2[0-4]\d
250-255     25[0-5]
"""

# 大佬鼠
import re
def is_valid_IP1(strng):
	return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))


import socket
def is_valid_IP2(addr):
	try:
		socket.inet_pton(socket.AF_INET, addr)
		return True
	except socket.error:
		return False

def is_valid_IP(strng):
	lst = strng.split('.')
	passed = 0
	for sect in lst:
		if sect.isdigit():
			if sect[0] != '0':
				if 0 < int(sect) <= 255:
					passed += 1
	return passed == 4