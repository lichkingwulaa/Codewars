def is_pangram(s):
    date = sorted(set(s.lower()))
    if "a" in date and "z" in date:
        return date.index("z") - date.index("a") == 25
    return False


print(is_pangram("1afghijklmnopqrstuvwxyzzzz"))
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
