from datetime import datetime

def elapsed_seconds(start, end):
	start = str(start).replace('-', ' ').replace(':', ' ').split(' ')
	end = str(end).replace('-', ' ').replace(':', ' ').split(' ')
	res = [ int(end[i]) - int(start[i]) for i in range(6) ]
	return res[2] * 86400 + res[3] * 3600 + res[4] * 60 + res[5]

start = datetime(2013, 1, 1, 0, 0, 1)
end = datetime(2013, 1, 1, 0, 0, 2)
print(elapsed_seconds(start, end))


# 大佬鼠
def elapsed_seconds(start, end):
	return (end-start).seconds