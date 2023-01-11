def title_case(title, minor_words=''):
	a = title.lower().split(' ')
	b = minor_words.lower().split(' ')
	return ' '.join([ a[i] if a[i] in b and i != 0 else a[i].title() for i in range(len(a)) ])



title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
title_case('', '')



# 大佬鼠
def title_case1(title, minor_words=''):
	title = title.capitalize().split()
	minor_words = minor_words.lower().split()
	return ' '.join([word if word in minor_words else word.capitalize() for word in title])

def title_case2(title, minor_words=''):
	return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))