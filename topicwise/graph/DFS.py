
# 链表
from collections import defaultdict 
class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):

		# 创建队列进行操作
		queue = []
		visited = [False]*(len(self.graph))

		# 存在则入队
		queue.append(s)
		visited[s] = True

		# 将邻边节点进行入队
		while queue:
			s = queue.pop(0)
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.BFS(2)
