def point(a, b):
	return lambda : [a, b]
def fst(pt):
	return pt()[0]
def snd(pt):
	return pt()[1]
def sqr_dist(pt1, pt2):
	x1, y1 = pt1()
	x2, y2 = pt2()
	return (x1 - x2) ** 2 + (y1 - y2) ** 2
def line(pt1, pt2):
	x1, y1 = pt1()
	x2, y2 = pt2()
	res = [y2 - y1, x1 - x2, (x2 - x1) * y1 - (y2 - y1) * x1]
	return res