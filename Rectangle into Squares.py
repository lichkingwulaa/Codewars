def sqInRect(lng, wdth):
	if lng == wdth:
		return None
	elif lng < wdth:
		lng,wdth = wdth,lng
	num = []
	while True:
		num.append(min(lng,wdth))
		lng = lng - wdth
		if lng < wdth:
			lng, wdth = wdth, lng
		elif num[-1] <= 0:
			return num[:-1]

print(sqInRect(5,11))




# 大佬鼠的迷惑方法
def sqInRect1(a, b):
	if a == b:
		return None
	res = []
	while b:
		b, a = sorted([a, b])
		res += [b]
		a, b = b, a - b
	return res