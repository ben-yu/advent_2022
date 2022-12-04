with open('./day_3_1.txt') as f:
	lines = f.readlines()
	score = 0
	for i in range(0, len(lines), 3):
		a, b, c = lines[i:i+3]

		common = set(list(a.strip())).intersection(set(list(b.strip()))).intersection(set(list(c.strip()))).pop()

		if common.isupper():
			val = ord(common) - ord('A') + 1 + 26
			score += val
		else:
			val = ord(common) - ord('a') + 1
			score += val
		#print(val)
		
	print(score)
