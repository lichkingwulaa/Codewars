"""
https://www.codewars.com/kata/faro-shuffle-count/python
"""
def faro_cycles(deck_size):
    old_num = num = [i for i in range(deck_size)]
    cur = 1
    while True:
        c = []
        for i in range(len(num) // 2):
            c.extend([num[i], num[i + len(num) // 2]])
        if c == old_num:
            return cur
        cur += 1
        num = c

print(faro_cycles(2),1)
print(faro_cycles(52),8)


def faro_cycles(n):
    x, cnt = 2, 1
    while x != 1 and n > 3:
        cnt += 1
        x = x*2 % (n-1)
    return cnt