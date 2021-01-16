import numpy, math

def gaussianReduction(vectors):
    if len(vectors)==2:
        v1=numpy.array(vectors[0])
        v2=numpy.array(vectors[1])
        while True:
            if numpy.dot(v2,v2) < numpy.dot(v1,v1):
                tmp = v1
                v1 = v2
                v2 =tmp
            m = math.floor(numpy.dot(v2,v1)/numpy.dot(v1,v1))
            if m==0:
                return [v1,v2]
            v2 = v2 - m*v1
    else:
        print("You must supply an array containing 2 vectors")

reducted = gaussianReduction( [[87502093, 123094980], [846835985, 9834798552]] )
r1 = reducted[0]
r2 = reducted[1]
print(r1[0]*r2[0]+r1[1]*r2[1])
print(numpy.dot(r1,r2))
