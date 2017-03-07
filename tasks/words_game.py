player_id = 1
word = ''
while not word.isalpha():
	word = input('Player #%d: ' % player_id)
	word = word.strip().upper()
words = {word}
last_char = word[-1]
player_id = 2
while True:
	word = input('Player #%d (%s): ' % (player_id, last_char))
	word = word.strip().upper()
	if word.isalpha():
		if word[0] == last_char:
			if word not in words:
				words.add(word)
				last_char = word[-1]
				player_id = player_id % 2 + 1 # 1-> 2 -> 1 -> 2 ...
			else:
				print('\aDuplicate word, it\'s still your turn.')
				continue
		else:
			print('\aWrong first letter, it\'s still your turn.')
			continue
	else:
		player_id = player_id % 2 + 1 # 1-> 2 -> 1 -> 2 ...
		word = input('Player #%d (%s): ' % (player_id, last_char))
		word = word.strip().upper() 
		if word.isalpha():
			if word[0] == last_char:
				if word not in words:
					words.add(word)
					print('\a\a\nCONGRATULATIONS! Player #%d wins the game!' % player_id)
					break
				else:
					print('\aDuplicate word, it\'s still your turn.')
					continue
			else:
				print('\aWrong first letter, it\'s still your turn.')
				continue
		else:
			print('\a\a\nDEAD HEAT!')
			break
