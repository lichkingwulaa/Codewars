import re
def name_in_str(string, name):
	s = ''.join(r'.*' + x.lower() for x in name)
	return bool(re.search(s, string.lower()))
# '.*'匹配除换行符以外的所有字符
print(name_in_str("Across the rivershahahah", "chris"))


# 大佬鼠
def name_in_str1(str, name):
	it = iter(str.lower())
	return all(c in it for c in name.lower())


from re import search; name_in_str2=lambda s,n: search(".*".join(list(n)),s,2) != None

import re
def name_in_str(str, name):
	return bool(re.search('.*'.join(name.lower()),str.lower()))