#coding:utf-8
"""
创建一个队列，用于存储检查的人
从队列弹出一个人
检查这人是否是要找的人
	若不是则将这人的所有邻居加入队列
若队列为空则无要找的人
O(V + E)

你需要按加入顺序检查搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必
须是队列。
对于检查过的人，务必不要再去检查，否则可能导致无限循环。
"""
"""
def search(name):
	search_queue = deque() 
	search_queue += graph[name] 
	searched = []
	while search_queue:
		person = search_queue.popleft() 
		if not person in searched:
			#这个数组用于记录检查过的人，仅当这个人没检查过时才检查
			if person_is_seller(person):
				print person + " is a mango seller!" 
				return True
			else:
				search_queue += graph[person] searched.append(person)
			return False
	#将这个人标记为检查过
 search("you")

 """
from collections import defaultdict

class Graph(object):

	"""docstring for graph"""
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)
		
	def BFS(self, s):
		# 创建队列和初始化记录采访过的数组
		queue = []
		visited = [False]*(len(self.graph))
		queue.append(s)
		visited[s] = True


        # 对邻边进行处理
		while queue:
			s = queue.pop(0)
			print(s, end='')
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



















