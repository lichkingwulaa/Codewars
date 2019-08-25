"""
https://www.codewars.com/kata/dubstep/train/python
"""
def song_decoder(song):
	song = song.split('WUB')
	song = [song[i] for i in range(len(song))  if song[i] != '']
	return ' '.join(song)

x = song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
print(x)

# 汪小佬
def song_decoder2(song):
	return ' '.join([song.split('WUB')[i] for i in range(len(song.split('WUB')))  if song.split('WUB')[i] != ''])

# 大佬鼠
def song_decoder3(song):
	return " ".join(song.replace('WUB', ' ').split())

# def split(self, sep=None, maxsplit=None)
# 当不给split函数传递任何参数时，分隔符sep会采用任意形式的空白字符：空格、tab、换行、回车以及formfeed
# maxsplit参数表明要分割得到的list长度