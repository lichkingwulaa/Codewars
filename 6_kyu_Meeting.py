def meeting(s):
	s = s.upper().split(';')
	ss = sorted(tuple(x.split(':')[::-1]) for x in s)
	sss = ['(' + ', '.join(x) + ')' for x in ss]
	return ''.join(sss)

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s),
      "\n(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)")


def meeting(s):
	ss = sorted(tuple(x.split(':')[::-1]) for x in s.upper().split(';'))
	return ''.join('(' + ', '.join(x) + ')' for x in ss)