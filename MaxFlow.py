# http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
# Ford-Fulkerson algorithm computes max flow in a flow network.
#
import text_to_array as t2a
"""
  nodes = t2a.convert_to_array.int_to_array('nodes.txt')
  edges = t2a.convert_to_array.int_to_array('edges.txt')
"""
capacities = t2a.convert_to_array.int_to_array('capacities.txt')

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

graph = capacities

g = Graph(graph)

source = 0 #Source is located at 0,0 in the graph
sink = 33 # Sink is located at 33,33 in the graph

print("Max Flow: %d " % g.ford_fulkerson(source, sink))