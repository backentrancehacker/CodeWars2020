import re
grid = []
for i in range(11):
	grid.append([' ']*11)

finishedWords = []
words = {}
possibleWords = []

file = open('input.txt', 'r')
lines = file.readlines()
file.close()
line = 0
# fill in grid paths
while lines[line] != '------\n':
	parts = lines[line].replace('\n', '').split(' ')
	length = int(parts[2])
	x = int(parts[3])
	y = int(parts[4])
	words[len(words)] = ["."*length, x, y, parts[1], len(words)]
	path = [1, 0]
	if (parts[1] == 'H'): path = [0, 1]
	for i in range(length):
		grid[y][x] = grid[y][x].strip() + parts[0]
		y += path[0]
		x += path[1]
	line += 1
line += 1
while lines[line] != '------\n':
	parts = lines[line].replace('\n', '').split(' ')
	x = int(parts[0])
	y = int(parts[1])
	wordnums = grid[y][x]
	grid[y][x] = parts[2]
	for w in wordnums:
		word = words[int(w)-1]
		if word[3] == 'V':
			yw = word[2]
			word[0] = word[0][:y-yw] + parts[2] + word[0][y-yw+1:]
		else:
			xw = word[1]
			word[0] = word[0][:x-xw] + parts[2] + word[0][x-xw+1:]
	line += 1
line += 1
while line < len(lines):
	possibleWords.append(lines[line].replace('\n', ''))
	line += 1

count = 0
while len(words) > 0:
	if count > len(possibleWords): break
	found = False
	for n in words:
		found = False
		w = words[n]
		pattern = re.compile(w[0])
		match = ''
		pindex = -1
		for p in range(len(possibleWords)):
			if pattern.match(possibleWords[p]):
				match = possibleWords[p]
				pindex = p
				break
		if not match: continue
		del possibleWords[pindex]
		w[0] = match
		x = w[1]
		y = w[2]
		path = [1, 0]
		if w[3] == 'H': path = [0, 1]
		for l in range(len(match)):
			wordnums = grid[y][x]
			
			for i in wordnums:
				if (not i.isdigit()) or int(i) == n: continue
				word = words[int(i)-1]
				if word[3] == 'V':
					yw = word[2]
					word[0] = word[0][:y-yw] + match[l] + word[0][y-yw+1:]
				else:
					xw = word[1]
					word[0] = word[0][:x-xw] + match[l] + word[0][x-xw+1:]
			grid[y][x] = match[l]
			y += path[0]
			x += path[1]
		finishedWords.append(w)
		found = n
		break
	if found != False: del words[found]
	count += 1

finishedWords.sort(key=lambda w: w[4])
for i in finishedWords:
	num = str(i[4]+1)
	if len(num) == 1: num = '0' + num

	print(num, 'is', i[0])
