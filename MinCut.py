
import numpy as np
import text_to_array as t2a

nodes = t2a.convert_to_array.int_to_array("data/nodes.txt")
edges = t2a.convert_to_array.int_to_array("data/edges.txt")

capacities = t2a.convert_to_array.int_to_array("data/capacities.txt")

class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])
        self.nodes = np.arange(len(graph)).reshape(-1,1)

    '''Returns true if there is a path from 
    source 's' to sink 't' in 
    residual graph. Also fills 
    parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of
            # the dequeued vertex u
            # If a adjacent has not been
            # visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    # If we reached sink in BFS starting
        # from source, then return
        # true, else false
        return True if visited[t] else False

    # Function for Depth first search
    # Traversal of the graph
    def dfs(self, graph, s, visited):
        visited[s] = True
        for i in range(len(graph)):
            if graph[s][i] > 0 and not visited[i]:
                self.dfs(graph, i, visited)

    # Returns the min-cut of the given graph
    def minCut(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

                # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        visited = len(self.graph) * [False]
        self.dfs(self.graph, s, visited)

        # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and \
                        self.org_graph[i][j] > 0 and visited[i]:
                    print(str(i) + " - " + str(j))
                    print("it works")

                # Create a graph given in the above diagram

graph = capacities

g = Graph(graph)

source = 0 #Source is located at 0,0 in the graph
sink = 33 # Sink is located at 33,33 in the graph

g.minCut(source, sink)

print(graph)

import networkx as nx
import matplotlib.pyplot as plt

def Zachary_graph():
    G = nx.Graph()
    rows = len(capacities)
    columns = len(capacities[0])
    for i in range(rows):
        for j in range(columns):
            if capacities[i][j] > 0:
                G.add_edge(i,j)


    nx.draw(G, with_labels=True)


    #Uncomment this section only when you want to see the graph
    plt.show()


    """
    # optional graph checkes are below  
    print(G.number_of_nodes())
    print(G.number_of_edges())
    print(nx.dominating_set(G, start_with=0))
    print(nx.dominating_set(G, start_with=33))
    """


    return G

G = Zachary_graph()
def predicted(G):
    G.nodes[0]["label"] = "A"
    G.nodes[33]["label"] = "B"
    predicted = nx.node_classification.harmonic_function(G, max_iter=1000)

    return predicted


def resulted(G):

    node_array = np.array(G.nodes)
    prediction = np.array(predicted(G))
    resulted = [None] * 34
    resulted = np.array(resulted)

    for i in range(len(node_array)):
        resulted[node_array[i]] = prediction[i]

    return resulted

"""
# Now, let's save the capacities of edges after the MinCut algorithm.

import json

with open('edgesafter.txt', 'w') as filehandle:
    json.dump(capacities.tolist(), filehandle)
"""