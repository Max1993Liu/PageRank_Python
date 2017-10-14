"""
Help functions to generate graphs based on a input text file.
The file should be in the form of: page1 -> page2, specifying a link from page1 to page2.
"""

from pagerank import *


def generate_graph(file):

	graph = Graph(set(), set())

	with open(file, 'r') as f:
		for line in f:
			line = line.split('->')
			if len(line) != 2:
				print('Skipping line: {}'.format('->'.join(line)))

			from_page_id, to_page_id = line
			from_page_id, to_page_id = from_page_id.strip(), to_page_id.strip()

			from_page, to_page = Page(from_page_id), Page(to_page_id)

			#add node and corresponding edge into the graph
			from_page = graph.add_node(from_page)
			to_page = graph.add_node(to_page)
			edge = Link(from_page, to_page)
			edge = graph.add_edge(edge)

			#configuring the in and out link for nodes and weight for edge
			from_page.add_outlink(edge)
			to_page.add_inlink(edge)
			edge.update_weight()

	return graph

