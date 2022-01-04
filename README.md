# Zachary-s-Karate-Club
This repo includes my trial to create the infamous Zachary's Karate Club dataset and apply some algorithms to understand how to cluster graph-shaped data.

edges.txt file includes the connections inbetween nodes in the Karate Club.
capacities.txt file includes the weights of connections (edges) for every single connection
nodes.txt file contains the nodes from 1 to 34

MaxFlow.py is nothing but an implementation of Ford-Fulkerson Algorithm onto my Zachary's Karate Club dataset.

I have just created these datasets and read them from txt. I have been applying some algorithms like Ford-Fulkerson (https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm), and MaxFlow (https://gist.github.com/bigsnarfdude/61c774506a9aa9938a933bc9189f74f0) to understand how to cope with graph-based data.

As of January 4th, I have visualized the graph right after I applied maximum-flow minimum-cut algorithm. I have used networkx for graph generation and visualization.

KarateClubAfterMinCut.png file contains the final graph after the network flow algorithm was applied. Please note that, node number 0 stands for Mr. Hi and node number 33 stands for the Officers'.
