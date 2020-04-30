from sys import exit,argv

class Vertex:

	def __init__(self,label):
		self.label = label
		self.color = None
		self.neighbours = []

	def __eq__(self,other):
		return self.label == other.label

	def __ne__(self,other):
		return self.label != other.label

	def connect_vertex(self,vertex):
		if vertex not in self.neighbours:
			self.neighbours.append(vertex)
		if self not in vertex.neighbours:
			vertex.neighbours.append(self)

		# Since for undirected graph
		return (Edge(self,vertex),Edge(vertex,self))

	def show_neighbours(self):
		print("Vertex {} neighbours".format(self.get_label()),end='')
		for vertex in self.neighbours:
			print(" {}".format(vertex.get_label()),end='')

		print()

	def get_label(self):
		return self.label


class Edge:
	
	def __init__(self,u,v):
		self._from = u
		self.to_ = v

	def __eq__(self,other):
		return (self._from == other._from) and (self.to_ == other.to_)

	def __ne__(self,other):
		return (self._from != other._from) and (self.to_ != other.to_)

class Graph:

	def __init__(self):
		self.vertices = []
		self.edges = []

	# only add a vertex if it does not exist in the graph
	def add_vertex(self,vertex):
		for v in self.vertices:
			if vertex == v:
				print("Vertex {} already exists in the graph".format(vertex.get_label()))
				return -1

		self.vertices.append(vertex)

	def add_edge(self,edge):
		for e in self.edges:
			if edge == e:
				print("Edge {} -- {} already exists in the graph".format(edge._from.get_label(),
											 edge.to_.get_label()))
				return -1

		self.edges.append(edge)

	def show_connections(self):
		print("Graph\n")
		for edge in self.edges:
			print("{} -- {}".format(edge._from.get_label(),edge.to_.get_label()))


	def save(self,fname):
		with open(fname,"w") as f:
			for edge in self.edges:
				f.write("{} -- {}\n".format(edge._from.get_label(),edge.to_.get_label()))

	def load(self,fname):
		graph = Graph()
		vertices = []
		with open(fname,"r") as f:
			for line in f:
				tokens = line.split(" -- ")
				tokens[1] = tokens[1].strip("\n")
				try:
					u = Vertex(tokens[0])
					v = Vertex(tokens[1])
					graph.add_vertex(u)
					graph.add_vertex(v)
					e1,e2 = u.connect_vertex(v)
					graph.add_edge(e1)	
					graph.add_edge(e2)	
				except Exception as e:
					print(str(e))

			graph.show_connections()		

def main():
	if argv[1] == "test":
		a = Vertex('a')
		b = Vertex('b')
		c = Vertex('c')
		d = Vertex('d')
		vertices = [a,b,c,d]
		graph = Graph()

		# Connections
		e1,e2 = a.connect_vertex(b)
		graph.add_edge(e1)
		graph.add_edge(e2)
	
		e1,e2 = b.connect_vertex(c)
		graph.add_edge(e1)
		graph.add_edge(e2)
	
		e1,e2 = c.connect_vertex(d)
		graph.add_edge(e1)
		graph.add_edge(e2)
	
		print("Showing Neighbours")
		for vertex in vertices:
			vertex.show_neighbours()
			graph.add_vertex(vertex)
	
		graph.save("graph_test.g")

	elif argv[1] == "load":
		try:
			graph = Graph()
			fname = argv[2]
			graph.load(fname)
		except Exception as e:
			print("No file name specified")
			print(str(e))
			exit()
			
		
	
if __name__ == "__main__":
	main()
