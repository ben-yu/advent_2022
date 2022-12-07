from collections import defaultdict
import re


class Directory:
	def __init__(self, cur_path, parent = None):
		self.parent = parent
		self.children = []
		self.size = 0
		self.dir_name = cur_path

visited = [] # List for visited nodes.
queue = []     #Initialize a queue


def bfs(visited, node, solution): #function for BFS
	visited.append(node)
	queue.append(node)

	while queue:          # Creating loop to visit each node
		m = queue.pop(0) 

		for n in m.children:
			m.size += n.size
			if n.dir_name not in visited:
				visited.append(n)
				queue.append(n)
		if m.size <= 100000:
			print("DIR: {} SIZE: {}".format(m.dir_name, m.size))
			solution += m.size
	return solution


visited = set()
size_arr = {}
def dfs(visited, node, solution, size_arr):  #function for dfs 
	if node not in visited:
		visited.add(node)
		for n in node.children:
			size, solution, size_arr = dfs(visited, n, solution, size_arr)
			node.size += size
		print("DIR: {} SIZE: {}".format(node.dir_name, node.size))
		size_arr[node.dir_name] = node.size
	if node.size <= 100000:
		solution += node.size
	return node.size, solution, size_arr


with open('./day_7_1.txt') as f:
	cur_path = []

	lines = f.readlines()

	root_directory = Directory('/')
	cur_directory = root_directory
	i = 1
	while i < len(lines):
		if i >= len(lines):
			break
		line = lines[i]
		print(line)
		#print("Current Dir {}".format(cur_directory))
		if line.startswith('$'):
			if 'cd' in line:
				#print(line)
				result = re.findall(r'([\S]+).+(\b[\w]+\b)\s+([a-zA-z\.]+)', line)

				dest = result[0][2]
				
				if dest == '..':
					#cur_path.pop()
					cur_directory = cur_directory.parent
				else:
					#cur_path.append(dest)
					d = Directory(dest, parent=cur_directory)
					dir_found = False
					for x in cur_directory.children:
						if dest == x.dir_name:
							cur_directory = d
					if not dir_found:
						cur_directory.children.append(d)
						cur_directory = d
			elif 'ls' in line:
				#print("LS {}".format(line))
				cur_directory.size = 0
				while True:
					i += 1
					if i >= len(lines):
						break
					line = lines[i]
					#print(">>>> {}".format(line))
					if '$' in line:
						i -= 1
						break
					
					result = re.findall(r'(\b\d+\b).+(\b\w+\b)', line)
					if len(result) > 0:
						cur_directory.size += int(result[0][0])
		i += 1
		
solution = 0
total, solution, size_arr = dfs(visited, root_directory, solution, size_arr)
disk_remaining = 70000000 - total
size_required = 30000000 - disk_remaining

print(size_required)
print(size_arr)

min_size = 70000000
for x in size_arr.keys():
	if size_arr[x] > size_required and size_arr[x] < min_size:
		min_size = size_arr[x]

print(min_size)