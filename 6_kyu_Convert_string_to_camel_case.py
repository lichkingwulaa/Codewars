import re

def to_camel_case(text):
	text = re.sub(r'[-_]', ' ', text).split(' ')
	return ''.join([text[i].title() if i >0 else text[i] for i in range(len(text))])

print(to_camel_case("a-Cat-Was_Pippi"))



# 大佬鼠
def to_camel_case1(s):
	return s[0] + s.title().translate(None, "-_")[1:] if s else s


import re
def to_camel_case2(text):
	return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)


def to_camel_case3(text):
	return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''