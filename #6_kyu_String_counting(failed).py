import itertools,time
a = time.time()

def solve(s,num = 0):
	# return sum(1 if s < ''.join(x) and s[::-1] < ''.join(x)[::-1] else 0
	#            for x in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ',repeat=len(s)))
	for x in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ',repeat=len(s)):
		if s < ''.join(x) and s[::-1] < ''.join(x)[::-1]:
			num += 1
	return num

print(solve("XYZ"),5)
print(solve("ABC"),16174)
print(solve("ABCD"),402230)
print(solve("ZAZ"),25)
print(solve("XYZA"),34480)

b = time.time()
print(b-a)

print(ord('A'), ord('Z'))