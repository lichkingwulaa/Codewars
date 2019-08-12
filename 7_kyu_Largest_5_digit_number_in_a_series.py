def solution(digits):
	return max([int(digits[i:i + 5]) for i in range(len(digits) - 4)])


number = "1234567898765"
print(solution(number))