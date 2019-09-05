from time import time
a = time()

def find_x0(n):
    if n == 0: return 0
    x = 0
    for i in range(1, n+1):
        x += find_x(i-1) + 3*i
    return x

def find_x(n):
    if n == 0: return 0
    x = 0
    for i in range(1, n+1):
        x += find_x(i - 1) + 3 * i
    return x


num = {}
for i in range(81057):
    num[str(i)] = find_x(i)

print(find_x(81057))

b = time()
print(b-a)