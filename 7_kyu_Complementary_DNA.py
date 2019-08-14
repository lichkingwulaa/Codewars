def DNA_strand(dna):
	d = { 'A': 'T', 'T': 'A',  'G': 'C',  'C': 'G' }
	return ''.join( d[x] for x in dna)

print(DNA_strand("ATTGC"))


# 大佬鼠
def DNA_strand(dna):
	return dna.translate(str.maketrans('ATGC', 'TACG'))