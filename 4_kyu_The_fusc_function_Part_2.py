def F(n, a, b):
    while n >= 2:
        if (n % 2) == 0:
            a, b = a+b, b
        else:
            a, b = a, a+b
        n //= 2

    if n == 0:
        return b
    else:
        return a+b


def fusc1(n):
    if n <= 1:
        return n
    while (n % 2) == 0:
        n //= 2
    return F(n // 2, 1, 1)


print(fusc1(85))

print(fusc1(0))
print(fusc1(1))
print(fusc1((1<<1000) + 1))
print(fusc1((1<<1000) - 1))
print(fusc1((1<<1000) + 5))
print(fusc1((1<<1000) + 21))