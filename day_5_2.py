import re
stacks = {
	1: ['R','N','F','V','L','J','S','M'],
	2: ['P','N','D','Z','F','J','W','H'],
	3: ['W','R','C','D','G'],
	4: ['N','B','S'],
	5: ['M','Z','W','P','C','B','F','N'],
	6: ['P','R','M','W'],
	7: ['R','T','N','G','L','S','W'],
	8: ['Q','T','H','F','N','B','V'],
	9: ['L','M','H','Z','N','F']
}


with open('./day_5_1.txt') as f:
	lines = f.readlines()
	for line in lines:
		pair = line.strip().split(',')
		result = re.findall(r'(\b\d+\b).+(\b\d+\b).+(\b\d+\b)', line)

		count, source_stack, dest_stack = int(result[0][0]), int(result[0][1]), int(result[0][2])

		removed_stack = stacks[source_stack][-count:]
		stacks[dest_stack].extend(removed_stack)
		del stacks[source_stack][len(stacks[source_stack]) - count:]

	message = []
	for i in range(1,10):
		message.append(stacks[i].pop())

	print("".join(message))