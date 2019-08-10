def dic_of_str_num(poly_list):
	"""将多项式拆分为"字母：系数"的键值对，并返回一个字典"""
	poly_dic = {}
	for poly in poly_list:      # 初始化以多项式为键的字典
		poly_str = ''.join(filter(lambda x: ord('A') <= ord(x) <= ord('z'), sorted(poly)))
		poly_dic[poly_str] = 0
	for poly in poly_list:      # 填入多项式的系数
		poly_str = ''.join(filter(lambda x: ord('A') <= ord(x) <= ord('z'), sorted(poly)))
		poly_num = ''.join(filter(lambda x: ord('0') <= ord(x) <= ord('9') or ord(x) == ord('-'), sorted(poly)))
		if poly_num == '':
			poly_dic[poly_str] += 1
		elif poly_num == '-':
			poly_dic[poly_str] -= 1
		else:
			poly_dic[poly_str] += int(poly_num)
	return poly_dic

def right_orser(poly_dic):
	"""按照顺序将字典的键值对进行合并"""
	key = [k for k, v in poly_dic.items() if v != 0]
	for i in range(len(key) - 1):       # 冒泡排序
		for j in range(len(key) - 1):
			if len(key[j]) > len(key[j + 1]):
				key[j], key[j + 1] = key[j + 1], key[j]
			elif len(key[j]) == len(key[j + 1]):
				key[j], key[j + 1] = sorted([key[j + 1], key[j]])
	for i in range(len(key)):           # 添加多项式的系数
		if str(poly_dic[key[i]]) == '1':
			continue
		elif str(poly_dic[key[i]]) == '-1':
			key[i] = '-' + key[i]
		else:
			key[i] = str(poly_dic[key[i]]) + key[i]
	return key

def simplify(poly):
	poly = poly.replace('+', ' ').replace('-', ' -')
	poly_list = [x for x in poly.split(' ') if x]       # 拆分多项式
	poly_dic = dic_of_str_num(poly_list)                # "字母：系数"键值对的字典
	key = right_orser(poly_dic)                         # 多项式按顺序排列后的各项
	result = '+'.join(k for k in key)                   # 将各项连接为字符串
	return result.replace('+-', '-')                    # 返回结果


print(simplify('-a+5ab+3a-c-2a'))


# 大佬鼠的迷惑方法
import re
def simplify(poly):
	p = {}
	for m in re.findall(r'([+-]?)(\d*)([a-z]+)', poly):
		var = ''.join(sorted(m[2]))
		p[var] = p.get(var,0)+(-1 if m[0]=='-' else 1)*(int(m[1]) if m[1]!='' else 1)
	poly = ''.join('+-'[p[k]<0]+str(abs(p[k]))+k for k in sorted(p, key=lambda x:(len(x),x)) if p[k])
	return re.sub('([+-])1(?=[a-z])',r'\1', poly)[poly[0]=='+':]