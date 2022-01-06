import numpy as np
import MinCut


real = ['A', 'A', 'A', 'A',
        'A', 'A', 'A', 'A', 'B',
        'B', 'A', 'A', 'A', 'A',
        'B', 'B', 'A', 'A', 'B',
        'A', 'B', 'A', 'B', 'B',
        'B', 'B', 'B', 'B', 'B',
        'B', 'B', 'B', 'B', 'B']
"""
real labels have been constructed from the data described in Wayne Zachary's paper published in 1977.
"""

data = np.array(real)
G = MinCut.Zachary_graph()
predicted = MinCut.resulted(G)
print(predicted)
correct = 0
"""
Previously, I have misinterpreted the output of harmonic_function which clustered the nodes as A and B.
In the first time, the classifier function gave the output in a random order. After a while, I figured out
that I needed to sort the nodes and check which class they were belonged to. The function called "resulted()" which was
written by me takes the predicted node labels and then sort them out according to the node numbers. Hence, I became able
to calculate accuracy in the proper way.

"""
for i in range(len(real)):
        if real[i] == predicted[i]:
                correct += 1
miss = len(real)-correct
accuracy = correct/len(real)
print("Accuracy is %f " %accuracy)
print("Hits are %d and misses are %d" %(correct,miss))