def find_it(seq):
	res = [sorted(seq)[i] for i in range(0, len(seq) - 1, 2) if sorted(seq)[i] != sorted(seq)[i + 1] ]
	return sorted(seq)[-1] if res == [] else res[0]

print(find_it([5,5,4,4,5,20,20]))

# 汪小佬
def find_it(seq):
	return list(x for x in seq if  seq.count(x) % 2 != 0)[0]
	
	pass

print(find_it([5,1,5,4,1,4,5,20,20]))

# 大佬鼠
import operator
from functools import reduce
def find_it(xs):
	return reduce(operator.xor, xs)