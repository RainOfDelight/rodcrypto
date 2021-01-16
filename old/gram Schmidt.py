"""
Algorithm for Gram-Schmidt
u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop

To test your code, let's grab the flag. Given the following basis vectors:
v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5),
use the Gram-Schmidt algorithm to calculate an orthogonal basis. The flag is the float value of the second component of u4 to 5 significant figures.

"""
import numpy as np
x1=[4,1,3,-1]
x2=[2,1,-3,4]
x3=[1,0,-2,7]
x4=[6,2,9,-5]
inputs=[x1,x2,x3,x4]

def gramSchmidth(inputs):
    size = len(inputs)
    results =[]
    results.append(np.array(inputs[0]))
    for calculating in range(1,size):
        partialResult=np.array(inputs[calculating])
        for i in range(0,calculating):
            proportion = np.dot(inputs[calculating],results[i])/np.dot(results[i],results[i])
            partialResult = partialResult - proportion*results[i]
        results.append(partialResult)
    return results

def createNormalVector(vector):
    size = np.sqrt(np.dot(vector,vector))
    return [elem/size for elem in vector]

normalized = createNormalVector([1,2,3])
print("Original size", np.dot([1,2,3],[1,2,3]), "Normalized size ", np.dot(normalized,normalized))
for elem in gramSchmidth(inputs):
    print(elem)