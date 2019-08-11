def spin_words(sentence):
	s = sentence.split(' ')
	for i in range(len(s)):
		if len(s[i]) >= 5:
			s[i] = s[i][::-1]
	return ' '.join(s)

print(spin_words('and or of one the one function returns in the'))

# 大佬鼠
def spin_words(sentence):
	return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])