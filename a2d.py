class Graph:

	def __init__(self,number_of_verts):
		self.graphVertices = number_of_verts
		self.edges = 0
		self.graph = [[None for _ in range(self.graphVertices)] for _ in range(self.graphVertices)]

	def add_vertex(self):
		graph2 = [[None for _ in range(self.graphVertices+1)] for _ in range(self.graphVertices+1)]

		for a in range(self.graphVertices):
			for b in range(self.graphVertices):
				graph2[a][b] = self.graph[a][b]
		self.graph = graph2
		self.graphVertices+=1

	def add_edge(self,from_idx, to_idx, weight = 1 ): # left keep the from as Y index and to as X index
		# we have to know that from_idx is Y axis of 2d array and to_idx is X axis of 2d array. Thus, if we start from one Y axis and 
		#keep going right to X axis, if value is not zero, means we find those edges who point towards to_idx
		if (from_idx < self.graphVertices and from_idx >= 0):
			if (to_idx < self.graphVertices and to_idx >= 0):
				if (self.graph[from_idx][to_idx] == None):
					self.graph[from_idx][to_idx] = weight
					self.edges+=1
					return True
		return False

	def num_edges(self):
		return self.edges

	def num_verts(self):
		return self.graphVertices

	def has_edge(self, from_idx,to_idx):
		if (from_idx < self.graphVertices and from_idx >= 0):
			if (to_idx < self.graphVertices and to_idx >= 0):
				if (self.graph[from_idx][to_idx] != None):
					return True
		return False

	def edge_weight(self, from_idx,to_idx):
			if (from_idx < self.graphVertices and from_idx >= 0):
				if (to_idx < self.graphVertices and to_idx >= 0):
					if (self.graph[from_idx][to_idx] != None):
						return self.graph[from_idx][to_idx]
			return None

	def get_connected(self, v):
		arrayOfTup = []
		for x in range(self.graphVertices):
			if (self.graph[v][x] != None):
				arrayOfTup.append((x, self.graph[v][x])) # returns vertex connected to v and its weight
		return arrayOfTup
	

	def get_edges(self):
		edges = []
		for from_idx in range(self.graphVertices):
			for to_idx in range(self.graphVertices):
				if self.graph[from_idx][to_idx] is not None:
					edges.append((from_idx, to_idx, self.graph[from_idx][to_idx]))
		return edges 
	
	
