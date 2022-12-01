
with open('./day_1_1.txt') as f:
	elves = []	
	lines = f.readlines()
	cur_calories = 0
	for line in lines:
		if line != "\n":
			cur_calories += int(line)
		else:
			elves.append(cur_calories)
			cur_calories = 0
			
	elves.sort()		
	print(sum(elves[-3:]))
