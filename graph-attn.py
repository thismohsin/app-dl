import numpy as np

class Node:
    def __init__(self):
        # Vector stored at this node
        self.data = np.random.randn(20)
        # Weights governing Q, K, V, how this node interacts with other nodes
        self.wkey = np.random.randn(20, 20)
        self.wquery = np.random.randn(20, 20)
        self.wvalue = np.random.randn(20, 20)

    def key(self):
        # What do I have
        return self.wkey @ self.data
    
    def query(self):
        # What I am looking for
        return self.wquery @ self.data

    def value(self):
        # What do I publicly reveal/broadcast
        return self.wvalue @ self.data

class Graph:
    def __init__(self):
        self.nodes = [Node() for _ in range(10)]
        # Make 40 edges
        randi = lambda: np.random.randint(len(self.nodes))
        self.edges = [(randi(), randi()) for _ in range(40)]

    def attention(self):
        updates = []
        for node in self.nodes:
            # Iterate over the edges (0, 1), (0, 2), and (1, 3).
            # Check if the source node index i is equal to node_index (which is 0).
            # Collect the target nodes self.nodes[1] and self.nodes[2] 
            # because the edges (0, 1) and (0, 2) have 0 as the source node.
            inputs = [self.nodes[j] for i, j in self.edges if i == self.nodes.index(node)]
            if not inputs:
                updates.append(np.zeros_like(node.data))
                continue
            keys = [m.key() for m in inputs]
            scores = [k.dot(node.query()) for k in keys]
            scores = np.exp(scores)
            scores = scores / np.sum(scores)
            values = [m.value() for m in inputs]
            update = sum([s * v for s, v in zip(scores, values)])
            updates.append(update)
        for n, u in zip(self.nodes, updates):
            n.data = n.data + u # residual connection

    def update(self):
        # Update the graph by performing attention
        self.attention()

# Example usage
graph = Graph()
print("Initial node data:")
for i, node in enumerate(graph.nodes):
    print(f"Node {i}: {node.data}")

graph.update()

print("\nUpdated node data:")
for i, node in enumerate(graph.nodes):
    print(f"Node {i}: {node.data}")
