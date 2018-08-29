from Stack import *         # We get all functions of Stack class.
from copy import  deepcopy

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.distance = -1
        self.visited = False                    # different from BFS

    def addAdjacent(self, adjacentNode):
        self.adjacents.append(adjacentNode)


class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)


# https://www.youtube.com/watch?v=bIA8HEEUxZI
def depthFirstSearchAlternative(Graph, sourceVertex):
    stack = Stack()                         # Created empty stack

    stack.push(sourceVertex)
    sourceVertex.visited = True             # Marked it as visited.
    print(sourceVertex.name)

    while not stack.isEmpty():
        node = stack.getTopItem()

        for adjNode in node.adjacents:      # Check if there is ANY "unvisited adjacent node".
            if adjNode.visited == False:
                stack.push(adjNode)
                adjNode.visited = True      # Marked it as visited.
                print(adjNode.name)
                break      # Repeat these steps for item which we've just added and is at the top of Stack.
        else:              # If node has no adjacents, then pop it from Stack.
            stack.pop()


def depthFirstSearch(Graph, sourceVertex):
    stack = Stack()                         # created empty stack

    stack.push(sourceVertex)

    while not stack.isEmpty():

        # for item in stack.items:    # to see inside of stack.
        #    print(item.name)

        node = stack.pop()

        if not node.visited:
            node.visited = True
            print(node.name)

            for n in node.adjacents:
                stack.push(n)










# ---   Creating Nodes and Relations
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.addAdjacent(b)
a.addAdjacent(e)

b.addAdjacent(c)
b.addAdjacent(d)

c.addAdjacent(b)
c.addAdjacent(d)

d.addAdjacent(b)
d.addAdjacent(c)

e.addAdjacent(f)
# ---   Creating Nodes and Relations


# Creating Graph
graph = Graph()
graph.addNode(a)
graph.addNode(b)
graph.addNode(c)
graph.addNode(d)
graph.addNode(e)
graph.addNode(f)
# Creating Graph


sourceNode = a
nodeName = input("Enter the node's name! Capital Letter! \t")
for node in graph.nodes:
    if (nodeName == node.name):
        sourceNode = node



alternativeGraph = deepcopy(graph)
alternativeSourceNode = deepcopy(sourceNode)
print("ALTERNATIVE STARTING FROM ", alternativeSourceNode.name)
depthFirstSearchAlternative(alternativeGraph, alternativeSourceNode)

print("THE VISITING ORDER OF NODES STARTING FROM ", sourceNode.name)
depthFirstSearch(graph, sourceNode)

