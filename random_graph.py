"""
Generating a random graph for testing
"""

import random

OUTPUT_FILE = './random_data.txt'
n_nodes = 100
n_edges = 130

graph_data = set()

while len(graph_data) <= n_edges:
	next_edge = (random.randint(1, n_nodes), random.randint(1, n_nodes))
	if next_edge[0] == next_edge[1]:
		continue
	graph_data.add(next_edge)


graph_data = ['{} -> {}'.format(l, r) for l, r in graph_data]


with open(OUTPUT_FILE, 'w') as f:
	f.writelines('\n'.join(graph_data))






