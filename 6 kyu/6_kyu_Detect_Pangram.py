def is_pangram(s):
    date = list(set(list(s.lower())))
    date.sort()
    if "a" in date and "z" in date and date.index("z") - date.index("a") == 25:
        return True
    return False



print(is_pangram("1afghijklmnopqrstuvwxyzzzz"))
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
