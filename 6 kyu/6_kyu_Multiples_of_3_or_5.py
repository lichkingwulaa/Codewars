def solution(number):
	return sum(x for x in range(1, number) if x % 3 == 0 or x % 5 == 0)

print(solution(10))

# 大佬鼠
def solution(number):
	a3 = (number-1)/3
	a5 = (number-1)/5
	a15 = (number-1)/15
	return (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15