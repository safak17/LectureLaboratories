from Queue import *         # We get all functions of Queue class.

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.distance = -1
        self.parent = None

    def addAdjacent(self, adjacentNode):
        self.adjacents.append(adjacentNode)

    def addParent(self, parentNode):
        self.parentNode = parentNode


class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)



def breadthFirstSearch(Graph, sourceVertex):
    queue = Queue()                         # created empty queue

    sourceVertex.distance = 0               # marked it as visited. (Its distance different from -1 ).
    queue.enqueue(sourceVertex)             # sourceVertex added to the queue in order to visit its adjacents.

    while queue.size() > 0:
        visitedNode = queue.dequeue()

        for adjNode in visitedNode.adjacents:
            if adjNode.distance == -1:           # if adjacent node was not visited.
                adjNode.distance = visitedNode.distance + 1     # Marked it as visited.
                # adj.parent = visitedNode
                print(adjNode.name)
                queue.enqueue(adjNode)           # adjacent node is added to the queue. Later, its adjacents will be visited.





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


print("THE NODES WHICH CAN BE VISITED BY ", sourceNode.name)
breadthFirstSearch(graph, sourceNode)
