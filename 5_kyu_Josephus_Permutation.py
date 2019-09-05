def josephus(items,k):
	res = []
	i = k - 1
	while items:
		i = i % len(items)
		res.append(items.pop(i))
		i += (k - 1)
	return res


print(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])
print(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
print(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
print(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
print(josephus([],3),[])