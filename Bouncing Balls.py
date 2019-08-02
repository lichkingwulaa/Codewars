def bouncingBall(h, bounce, window):
	if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
		return -1
	i = 0
	while h*bounce > window:
		i += 2
		h *= bounce
	return i+1

print(bouncingBall(30, 0.66, 1.5))



# 大佬鼠
# 通项公式
# 设第n次在空中为an，则通项an=h*pow(b,n),an>0，解出n，共有(2n+1)次
from math import log
def bouncingBall(h, bounce, window):
	if not (h > 0 and 0 < bounce < 1 and window < h):
		return -1
	return 1 + 2*int(log(window/float(h), bounce))