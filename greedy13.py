# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print('节点1到节点', node+1, "的距离是", dist[node])

    def minDistance(self, dist, sptSet):
        # dist:[0, 9223372036854775807,9223372036854775807,9223372036854775807,9223372036854775807]
        # sptSet：[false, false, false, false, false] # 找到单行最小的值
        min = sys.maxsize
        for v in range(self.V):
            # 找到当前的最小值，记住所在行
            # 判断其值 小于最小值 和他的False
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                # 对于有值且未走的节点，计算每个小于原有值
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

# Driver program
g = Graph(5)

g.graph = [[0, 10, 0, 0, 5],
            [0, 0, 1, 0, 2],
            [0, 0, 0, 4, 0],
            [7, 0, 6, 0, 0],
            [0, 3, 9, 2, 0]
            ]
g.dijkstra(0)

# This code is contributed by Divyanshu Mehta
