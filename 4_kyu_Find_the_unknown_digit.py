def solve_runes(runes):
	num_pick = [i for i in range(10) if str(i) not in runes]
	runes = runes.replace('--', '+').replace('+-', '-').replace('=', '==')
	if 0 in num_pick:
		for x in runes.replace('*', '+').replace('-', '+').replace('=', '+').replace('?', '0').split('+'):
			if x.isdigit() and len(x) > 1 and x[0] == '0':
				num_pick.remove(0)
				break
	for i in num_pick:
		runes_re = runes.replace('?', str(i))
		if eval(runes_re):
			return i
	return -1

print(solve_runes('??*1=??'))


# 大佬鼠
import re

def solve_runes1(runes):
	for d in sorted(set("0123456789") - set(runes)):
		toTest = runes.replace("?",d)
		if re.search(r'([^\d]|\b)0\d+', toTest): continue
		l,r = toTest.split("=")
		if eval(l) == eval(r): return int(d)
	return -1


def solve_runes2(runes):
	for c in sorted(set('0123456789') - set(runes)):
		s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
		if not any(e[0] == '0' and e != '0' for e in s.split()) and eval(s): return int(c)
	return -1