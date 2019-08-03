import re

reg = r'(?=.\*[A-Z].\*)(?=.\*[a-z].\*)(?=.\*\d.\*)[a-zA-Z0-9]{6,}'

a = re.compile('/Chapter [1-9][0-9]*/')
print(a)

# Failed 难受 没干出来