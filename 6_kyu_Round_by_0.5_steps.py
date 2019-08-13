def solution(n):
	return int(n) + (0 if n - int(n) < 0.25 else 0.5 if 0.25 <= n - int(n) < 0.75 else 1)



print(solution(4))
print(solution(4.2))
print(solution(4.25))
print(solution(4.3))

print(solution(4.6))
print(solution(4.75))
print(solution(4.8))


# 大佬鼠
def solution(n):
	return round(2 * n) / 2