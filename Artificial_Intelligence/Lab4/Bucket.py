from Stack import *

class Buckets:
    def __init__(self, bucket1, bucket2):
        self.volume = [bucket1, bucket2]
        self.inside = [0, 0]
        self.operationName = ""

    def print(self):
        print("Bucket1: ", self.inside[0], "\t\tBucket2: ", self.inside[1])

    def fill(self, bucketNumber):
        self.inside[bucketNumber-1] = self.volume[bucketNumber-1]
        self.operationName = str(bucketNumber) + "is filled."

    def empty(self, bucketNumber):
        self.inside[bucketNumber-1] = 0
        self.operationName = str(bucketNumber) + "is emptied."

    def transfer(self, sourceBucketNumber, destinationBucketNumber):
        emptyVolumeInDestination = self.volume[destinationBucketNumber-1] - self.inside[destinationBucketNumber-1]
        self.operationName = str(sourceBucketNumber) + " is transferred to " + str(destinationBucketNumber)
        if self.inside[sourceBucketNumber-1] <= emptyVolumeInDestination:
            self.inside[destinationBucketNumber - 1] += self.inside[sourceBucketNumber - 1]
            self.inside[sourceBucketNumber-1] = 0
        else:
            self.inside[sourceBucketNumber-1] -= emptyVolumeInDestination
            self.fill(destinationBucketNumber)

    def isFull(self, bucketNumber):
        return self.inside[bucketNumber-1] == self.volume[bucketNumber-1]

    def isEmpty(self, bucketNumber):
        return self.inside[bucketNumber-1] == 0


class Node:
    def __init__(self, bckt):
        self.buckets = Buckets(bckt.volume[0], bckt.volume[1])
        self.buckets.inside = []
        self.buckets.inside.append(bckt.inside[0])
        self.buckets.inside.append(bckt.inside[1])
        self.childNodes = []
        self.parent = None
        self.depth = 0
        self.visited = False

    def appendChild(self, node):
        self.childNodes.append(node)

    def addParent(self, parent):
        self.parent = parent


def createProbability(NODE, limitDepth):
    if not NODE.buckets.isFull(1):               # birinci kova dolu değilse
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        n.buckets.fill(1)
        NODE.appendChild(n)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)

    if not NODE.buckets.isFull(2):               # ikinci kova dolu değilse
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        NODE.appendChild(n)
        n.buckets.fill(2)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)

    if not NODE.buckets.isEmpty(1):               # birinci kova boş değilse, ikinciye aktarabilir
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        NODE.appendChild(n)
        n.buckets.transfer(1, 2)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)

    if not NODE.buckets.isEmpty(2):               # birinci kova boş değilse, ikinciye aktarabilir
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        NODE.appendChild(n)
        n.buckets.transfer(2, 1)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)

    if not NODE.buckets.isEmpty(1):               # birinci kova boş değilse, onu boşalt
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        NODE.appendChild(n)
        n.buckets.empty(1)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)

    if not NODE.buckets.isEmpty(2):               # ikinci kova boş değilse, ikinciyi boşalt
        n = Node(NODE.buckets)
        n.addParent(NODE)
        n.depth = NODE.depth + 1
        NODE.appendChild(n)
        n.buckets.empty(2)
        if n.depth != limitDepth:
            createProbability(n, limitDepth)


def depthFirstSearch(sourceVertex, goal):
    stack = Stack()                         # created empty stack

    stack.push(sourceVertex)

    while not stack.isEmpty():

        # for item in stack.items:    # to see inside of stack.
        #    print(item.name)

        np = stack.pop()

        if not np.visited:

            if np.buckets.inside[0] == goal or np.buckets.inside[1] == goal:
                return np

            np.visited = True
            for n in np.childNodes:
                stack.push(n)


volumeOfBucket1 = int(input("Please, enter the volume of first bucket:\t"))
volumeOfBucket2 = int(input("Please, enter the volume of second bucket:\t"))
goal = int(input("Enter the goal value:\t"))

buckets = Buckets(volumeOfBucket1, volumeOfBucket2)
node = Node(buckets)
depth = 3


createProbability(node, depth)

n = depthFirstSearch(node, goal)
flag = True
while n is None:
    depth = depth + 2
    print("Searching in depth of  " + str(depth))
    newNodeForNewTree = Node(buckets)
    createProbability(newNodeForNewTree, depth)
    n = depthFirstSearch(node, goal)

    if depth == 15:
        flag = False
        break

if flag:
    while n.parent != None:
         print("Depth of Node "+
               str(n.depth)+"  ["+
               str(n.buckets.inside[0])+","+
               str(n.buckets.inside[1])+"]"+
               "  Operation Name:"+
               n.buckets.operationName)
         n = n.parent
else:
    print("There is no solution in first "+str(depth)+" depth")
