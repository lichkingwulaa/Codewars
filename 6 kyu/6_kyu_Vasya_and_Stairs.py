"""
https://www.codewars.com/kata/vasya-and-stairs/python
"""
def numberOfSteps(steps, m):
    num = steps // 2 + steps % 2
    for i in range(num, steps + 1):
        if i % m == 0:
            return i
    return -1

print(numberOfSteps(10, 2), 6)
print(numberOfSteps(3, 5), -1)
