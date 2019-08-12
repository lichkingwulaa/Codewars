def solution(n):
	return eval("%.2f"% n)

solution(2.69448)

def solution1(n):
	return round(n, 2)

def solution2(n):
	return float('{:.2f}'.format(n))

def solution3(n):
	return float(format(n, '.2f'))

def solution(n):
	return int(n*100+0.5)/100