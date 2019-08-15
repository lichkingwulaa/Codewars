def zero(a=''): return eval('0' + a)
def one(a=''): return eval('1' + a)
def two(a=''): return eval('2' + a)
def three(a=''): return eval('3' + a)
def four(a=''): return eval('4' + a)
def five(a=''): return eval('5' + a)
def six(a=''): return eval('6' + a)
def seven(a=''): return eval('7' + a)
def eight(a=''): return eval('8' + a)
def nine(a=''): return eval('9' + a)

def plus(b): return '+' + str(b)
def minus(b): return '-' + str(b)
def times(b): return '*' + str(b)
def divided_by(b): return '//' + str(b)

print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three())) )# must return 5
print(six(divided_by(two()))) # must return 3


# 大佬鼠
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y



# 大佬鼠
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x


print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three())) )# must return 5
print(six(divided_by(two()))) # must return 3
