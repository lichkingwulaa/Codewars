def increment_string(strng):
	print(strng)
	for i in range(len(strng)):
		if strng[i:].isdigit():
			return strng[:i] + '0' * (len(strng[i:]) - len(str(int(strng[i:]) + 1))) + str(int(strng[i:]) + 1)
	return strng + '1'


print(increment_string("00"))


# 大佬鼠
def increment_string(strng):
	head = strng.rstrip('0123456789')
	tail = strng[len(head):]
	if tail == "": return strng+"1"
	return head + str(int(tail) + 1).zfill(len(tail))