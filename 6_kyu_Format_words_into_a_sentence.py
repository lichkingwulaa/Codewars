def format_words(words):
	print(words)
	if words is None:
		return ''
	words = [x for x in words if x]
	if not words:
		return ''
	return words[0] if len(words) == 1 else ', '.join(words[:-1]) + ' and ' + words[-1]



print(format_words(['']))

# 汪小佬
def format_words1(words):
	words = [x for x in words if x] if words else ''
	return '' if not words else words[0] if len(words) == 1 else ', '.join(words[:-1]) + ' and ' + words[-1]

# 大佬鼠
def format_words2(words):
	return ', '.join(word for word in words if word)[::-1].replace(',', 'dna ', 1)[::-1] if words else ''