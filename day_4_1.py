
def tuple_contains(a, b):
	if a[0] <= b[0] and a[1] >= b[1]:
		return True
	return False


def tuple_doesnt_overlap(a, b):
	if b[0] > a[1] or b[1] < a[0]:
		return True
	return False


with open('./day_4_1.txt') as f:

	contain_count = 0
	overlap_count = 0
	lines = f.readlines()
	cur_calories = 0
	for line in lines:
		pair = line.strip().split(',')
		a = tuple(map(lambda x: int(x), pair[0].split('-')))
		b = tuple(map(lambda x: int(x), pair[1].split('-')))

		#print("{} {}".format(a,b))
		if tuple_contains(a,b) or tuple_contains(b,a):
			contain_count += 1
		if not tuple_doesnt_overlap(a,b):
			overlap_count += 1			
		
	print(contain_count)
	print(overlap_count)
