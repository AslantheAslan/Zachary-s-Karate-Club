import numpy as np
import MinCut

real = ['A', 'A', 'A', 'A',
        'A', 'A', 'A', 'A', 'A',
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
predicted = MinCut.predicted(G)
correct = 0

for i in range(len(real)):
        if real[i] == predicted[i]:
                correct += 1
miss = len(real)-correct
accuracy = correct/len(real)
print("Accuracy is %f " %accuracy)
print("Hits are %d and misses are %d" %(correct,miss))