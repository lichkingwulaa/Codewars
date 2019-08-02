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
def song_decoder33(song):
	return " ".join(song.replace('WUB', ' ').split())