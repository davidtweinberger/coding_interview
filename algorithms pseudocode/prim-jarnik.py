#! /usr/bin/python

######################################
# PSEUDOCODE
# Prim-Jarnik algorithm to find a 
# Minimum Spanning Tree (MST) of a 
# graph with weighted edges
#
# IN: a weighted, undirected graph
# OUT: a minimum spanning tree (a 
# list of edges)

def prim_jarnik(graph):
	for vertex in graph.vertices:
		vertex.cost = infinity
		vertex.prev = null
	source = random.choice(graph.vertices)
	source.cost = 0

	MST = []

	PQ = PriorityQueue()
	PQ.add(v) for v in graph.vertices

	while not PQ.isEmpty():
		node = PQ.removeMin()
		if v.prev is not None:
			MST.append((v.prev, v))
		for incident_edge in graph.incidentEdges(node):
			neighbor = incident_edge.destination
			if neighbor.cost > incident_edge.weight:
				neighbor.cost = incident_edge.weight
				neighbor.prev = node
				PQ.replaceKey(neighbor, neighbor.cost)

	return MST

#RUNTIME is O((E+V)*log(V))