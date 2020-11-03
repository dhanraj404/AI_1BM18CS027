# Python program to print DFS traversal from a given 
# given graph 
from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 

		self.V = vertices 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	def DLS(self,src,target,maxDepth): 

		if src == target : return True
		if maxDepth <= 0 : return False
		for i in self.graph[src]: 
				if(self.DLS(i,target,maxDepth-1)): 
					return True
		return False

	def IDDFS(self,src, target, maxDepth): 
		for i in range(maxDepth): 
			if (self.DLS(src, target, i)): 
				return True
		return False



n = int(input("Enter The Number of Vertices"))	
g = Graph(n)


ed = int(input("Enter Number of egdes: "))
for _ in range(ed):
	print("Enter Edge",_,": ")
	start, end = map(int, input().split())
	g.addEdge(start, end)
target, maxDepth, src = map(int, input("Enter Target, Max Depth, Source:").split())
if g.IDDFS(src, target, maxDepth) == True: 
	print ("Target is reachable from source " +
		"within max depth") 
else : 
	print ("Target is NOT reachable from source " +
		"within max depth") 

"""
7

6

0 1
0 2
1 3
1 4
2 5
2 6

6 3 0

3


"""