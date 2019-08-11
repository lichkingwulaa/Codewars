def best_match(goals1, goals2):
	g = [goals1[i] - goals2[i] for i in range(len(goals1))]
	indexs = [i for i in range(len(g)) if g[i] == min(g)]
	for i in indexs:
		if goals2[i] == max([goals2[i] for i in indexs]):
			return i



goals1 = [4,3,4]
goals2 = [1,1,1]
print(best_match(goals1, goals2))



# 大佬鼠的迷惑方法 . What's the "-b" for?
def best_match1(goals1, goals2):
	return sorted( (a-b, -b, i) for i,(a,b) in enumerate(zip(goals1, goals2)) )[0][2]