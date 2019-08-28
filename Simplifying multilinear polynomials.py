import re
def simplify(poly):
	p = {}
	for x in  re.findall(r'([+-]?)(\d*)([a-z]+)', poly):
		var = ''.join(sorted(x[2]))
		p[var] = p.get(var, 0) + (-1 if x[0] == '-' else 1) * (int(x[1]) if x[1] != '' else 1)
	poly = '+'.join(str(p[x]) + x for x in sorted(p, key=len) if p[x])
	return re.sub(r'[+-]?1[a-z]')



print(simplify("dc+dcba"), "\ncd+abcd")
print(simplify("-a+5ab+3a-c-2a"),"\n-c+5ab")














def simplify1(poly):
	p = {}
	for m in re.findall(r'([+-]?)(\d*)([a-z]+)', poly):
		var = ''.join(sorted(m[2]))
		p[var] = p.get(var,0)+(-1 if m[0]=='-' else 1)*(int(m[1]) if m[1]!='' else 1)
	poly = ''.join('+-'[p[k]<0]+str(abs(p[k]))+k for k in sorted(p, key=lambda x:(len(x),x)) if p[k])
	return re.sub('([+-])1(?=[a-z])',r'\1', poly)[poly[0]=='+':]

print(simplify1("dc+dcba"), "\ncd+abcd")
print(simplify1("-a+5ab+3a-c-2a"),"\n-c+5ab")