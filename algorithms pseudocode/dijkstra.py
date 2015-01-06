#! /usr/bin/python


####################################################
# Pseudocode for Dijkstra's Algorithm (Graph Search)
# Takes in:
# 	- the graph
#	- the start node
#	- the destination node
# Returns the shortest path

def cs141_dijkstra(graph, start, destination):
	PQ = PriorityQueue()
	PQ.push(0, [start])

	V = {}

	while not PQ.isEmpty():
		cost, path = PQ.pop()
		node = path[-1]
		if node is not in V:
			V.add(node)
			if node is destination:
				return path
			for edge in graph.outgoingEdges(node)
				PQ.push(cost + edge.cost, path + [edge.destination])


####################################################
# Pseudocode - in place decorates nodes with dist
# and prev pointers to retrace a path.

def cs16_dijkstra(graph, start):
	for vertex in graph.vertices:
		vertex.dist = infinity
		vertex.prev = None
	s.dist = 0

	PQ = PriorityQueue()
	PQ.add(node.dist, node) for node in graph.vertices

	while not PQ.isEmpty():
		current = PQ.removeMin()
		for edge in graph.outgoingEdges(current)
			neighbor = edge.destination
			if neighbor.dist > current.dist + edge.cost:
				neighbor.dist = current.dist + edge.cost
				neighbor.prev = current
				PQ.replaceKey(neighbor, neighbor.dist)

# RUNTIME FOR THIS ONE IS O((V+E)*LOG(V)) DEPENDING ON THE IMPLEMENTATION OF THE PQ

def cs16_bellman_ford(graph, start):
	for vertex in graph.vertices:
		vertex.dist = infinity
		vertex.prev = null
	start.dist = 0
	for i in range(len(graph.vertices)-1):
		for s, d in graph.edges:
			if s.dist + cost(s, d) < d.dist:
				d.dist = s.dist + cost(s, d)
				d.prev = s

#RUNTIME IS O(V*E)


