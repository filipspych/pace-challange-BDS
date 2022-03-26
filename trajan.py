# source: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

from collections import defaultdict
from igraph import *


class Trajan:

	def __init__(self, g: Graph):
		self.g = g
		self.Time = 0
		
	def SCCUtil(self, u, low, disc, stackMember, st):

		# Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1
		stackMember[u] = True
		st.append(u)

		# Go through all vertices adjacent to this
		for e in self.g.es.select(_source=u):
			(a, b) = e.tuple
			if(a!=u): v = a
			else: v = b

			# If v is not visited yet, then recur for it
			if disc[v] == -1 :
			
				self.SCCUtil(v, low, disc, stackMember, st)

				# Check if the subtree rooted with v has a connection to
				# one of the ancestors of u
				# Case 1 (per above discussion on Disc and Low value)
				low[u] = min(low[u], low[v])
						
			elif stackMember[v] == True:

				'''Update low value of 'u' only if 'v' is still in stack
				(i.e. it's a back edge, not cross edge).
				Case 2 (per above discussion on Disc and Low value) '''
				low[u] = min(low[u], disc[v])

		# head node found, pop the stack and print an SCC
		w = -1 #To store stack extracted vertices
		if low[u] == disc[u]:
			while w != u:
				w = st.pop()
				print (w, end=" ")
				stackMember[w] = False
			print()
			
	

	#The function to do DFS traversal.
	# It uses recursive SCCUtil()
	def SCC(self):

		# Mark all the vertices as not visited
		# and Initialize parent and visited,
		# and ap(articulation point) arrays
		disc = [-1] * (self.g.vcount())
		low = [-1] * (self.g.vcount())
		stackMember = [False] * (self.g.vcount())
		st =[]
		

		# Call the recursive helper function
		# to find articulation points
		# in DFS tree rooted with vertex 'i'
		for i in range(self.g.vcount()):
			if disc[i] == -1:
				self.SCCUtil(i, low, disc, stackMember, st)


#This code is contributed by Neelam Yadav


tr = Trajan(Graph.Full(10))
tr.SCC()