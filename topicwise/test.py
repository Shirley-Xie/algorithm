
"""
带权路径问题，最快路径
Dijkstra：和广度搜索很像，这里不是标记是更新同一等级的数值，记住父节点。
Floyd：
"""
# A Python program for Dijkstra's shortest 
# path algorithm for adjacency 
# list representation of graph 

from collections import defaultdict 
import sys 

class Heap(): 

	# A utility function to swap two nodes 
	# of min heap. Needed for min heapify 

	# A standard function to heapify at given idx 
	# This function also updates position of nodes 
	# when they are swapped.Position is needed 
	# for decreaseKey() 
	def minHeapify(self, idx): 
		smallest = idx 
		left = 2*idx + 1
		right = 2*idx + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]: 
			smallest = left 

		if right < self.size and self.array[right][1] < self.array[smallest][1]: 
			smallest = right 

		# The nodes to be swapped in min 
		# heap if idx is not smallest 
		if smallest != idx: 

			# Swap positions 
			self.pos[ self.array[smallest][0] ] = idx 
			self.pos[ self.array[idx][0] ] = smallest 

			# Swap nodes 
			self.swapMinHeapNode(smallest, idx) 

			self.minHeapify(smallest) 

	# Standard function to extract minimum 
	# node from heap 
	def extractMin(self): 

		# Return NULL wif heap is empty 
		if self.isEmpty() == True: 
			return

		# Store the root node 
		root = self.array[0] 

		# Replace root node with last node 
		lastNode = self.array[self.size - 1] 
		self.array[0] = lastNode 

		# Update position of last node 
		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		# Reduce heap size and heapify root 
		self.size -= 1
		self.minHeapify(0) 

		return root 

	def isEmpty(self): 
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist): 

		# Get the index of v in heap array 
		i = self.pos[v]

		# Get the node and update its dist value 
		self.array[i][1] = dist 
		
		# Travel up while the complete tree is 
		# not hepified. This is a O(Logn) loop 
		while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 

			# Swap this node with its parent 
			self.pos[ self.array[i][0] ] = (i-1)//2
			self.pos[ self.array[(i-1)//2][0] ] = i 
			self.swapMinHeapNode(i, (i - 1)//2 ) 

			# move to parent index 
			i = (i - 1) // 2; 

	# A utility function to check if a given 
	# vertex 'v' is in min heap or not 
	def isInMinHeap(self, v): 

		if self.pos[v] < self.size: 
			return True
		return False

class Graph(): 
	def dijkstra(self, src): 

		# Make dist value of src vertex as 0 so 
		# that it is extracted first 
		minHeap.pos[src] = src 
		dist[src] = 0
		minHeap.decreaseKey(src, dist[src]) 

		# Initially size of min heap is equal to V 
		minHeap.size = V; 

		# In the following loop, min heap contains all nodes 
		# whose shortest distance is not yet finalized. 
		while minHeap.isEmpty() == False: 

			# Extract the vertex with minimum distance value 
			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0] 

			# Traverse through all adjacent vertices of 
			# u (the extracted vertex) and update their 
			# distance values 
			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 

				# If shortest distance to v is not finalized 
				# yet, and distance to v through u is less 
				# than its previously calculated distance 
				if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and pCrawl[1] + dist[u] < dist[v]: 
						dist[v] = pCrawl[1] + dist[u] 

						# update distance value 
						# in min heap also 
						minHeap.decreaseKey(v, dist[v]) 

		# printArr(dist,V) 


# Driver program to test the above functions 
graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.dijkstra(0) 

# This code is contributed by Divyanshu Mehta 
