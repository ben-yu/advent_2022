with open('./day_3_1.txt') as f:
	lines = f.readlines()
	score = 0
	for line in lines:
		line = line.strip()
		mid = int(len(line)/2)
		a = line[:mid]
		b = line[-mid:]
		print(a)
		print(b)

		common = set(list(a)).intersection(set(list(b))).pop()

		if common.isupper():
			val = ord(common) - ord('A') + 1 + 26
			score += val
		else:
			val = ord(common) - ord('a') + 1
			score += val
		#print(val)
		
	print(score)
