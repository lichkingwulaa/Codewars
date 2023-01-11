"""
https://www.codewars.com/kata/find-x/train/python
"""
def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += j + i
    return x



def findX(n):
    return n ** 2 * (3 * n - 2)