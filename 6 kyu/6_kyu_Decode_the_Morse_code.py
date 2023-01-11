morse = {   '.-': 'A',      '-...': 'B',    '-.-.': 'C',    '-..':'D',      '.':'E',      '..-.':'F',   '--.': 'G',
            '....': 'H',    '..': 'I',      '.---':'J',     '-.-': 'K',     '.-..': 'L',  '--': 'M',    '-.': 'N',
            '---': 'O',     '.--.': 'P',    '--.-': 'Q',    '.-.': 'R',     '...': 'S',   '-': 'T',
            '..-': 'U',     '...-': 'V',    '.--': 'W',     '-..-': 'X',    '-.--': 'Y',  '--..': 'Z',
            '..--..': '?',  '-.-.--':'!',   '.-.-.-': '.',  '': ' ',        '...---...': 'SOS',     }
def decodeMorse(morse_code):
	res = ''
	for x in morse_code.strip().split('  '):
		for y in x.split(' '):
			if y in morse.keys():
				res += morse[y]
			else:
				return None
	return res

print(decodeMorse('...---...'))


def decodeMorse(morse_code):
	return ''.join( morse[y]  for x in morse_code.strip().split('  ') for y in x.split(' ') )