def search_substr(full_text, search_text, allow_overlap=True):
	print(full_text, search_text, allow_overlap)
	if allow_overlap:
		count = 0
		for i in range(len(full_text) - len(search_text) + 1):
			if full_text[i:i + len(search_text)] == search_text != '':
				count += 1
		return count
	else:
		return full_text.count(search_text) if search_text else 0

print(search_substr('a', '', allow_overlap=True))

# 汪小佬
def search_substr1(full_text, search_text, allow_overlap=True):
	if allow_overlap:
		return len([search_text  for i in range(len(full_text) - len(search_text) + 1)
		            if full_text[i:i + len(search_text)] == search_text != '' ])
	else:
		return full_text.count(search_text) if search_text else 0

def search_substr2(full_text, search_text, allow_overlap=True):
	return len([search_text for i in range(len(full_text) - len(search_text) + 1)
	            if full_text[i:i + len(search_text)] == search_text != '']) \
		if allow_overlap else (full_text.count(search_text) if search_text else 0)

# 大佬鼠
import re
def search_substr(full_text, search_text, allow_overlap=True):
	if not full_text or not search_text: return 0
	return len(re.findall(f'(?=({search_text}))' if allow_overlap else search_text, full_text))